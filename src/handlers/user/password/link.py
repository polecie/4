from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from src.callbacks import BasicActions as ba
from src.callbacks import ConnectionType as ct
from src.keyboards import confirm_reset_keyboard, continue_repeat_keyboard
from src.states import ConnectionEForm as Form
from src.validators.email import CheckPost
from src.validators.password import CheckPasswords
from src.services.senders import SenderApiGateway, get_sender_gateway

__all__ = ("router",)

router = Router()  # роутер для обработки входа через пароль


@router.callback_query(Text(ct.password.value), Form.connection_type)
async def process_connection_via_password(cback: types.CallbackQuery, state: FSMContext):
    await state.update_data(connection_type=cback.data)
    await cback.message.edit_text(
        "Вы выбрали авторизацию через пароль для внешних приложений, "
        "далее вам необходимо прислать мне почту, которую вы хотите привязать\n\n"
        "Если вы хотите отменить действие на любом этапе привязки, "
        "нажмите /cancel и это вернет вас в главное меню"
    )
    await state.set_state(Form.post)


# TODO: добавить валидацию почты
@router.message(Form.post)
async def process_entered_email(message: types.Message, state: FSMContext):
    email = message.text
    data = await state.get_data()
    if CheckPost.check_format(email) and CheckPost.check_domain(email, data["provider"]):
        await state.update_data(email=message.text)
        await message.answer(
            "Отлично! Теперь проверьте правильность введенной вами почты и нажмите <b>Продолжить</b>, "
            "если все верно\n\n"
            f"Почта {message.text}",
            reply_markup=continue_repeat_keyboard.as_markup(),
        )
        await state.set_state(Form.check_post)
        await message.delete()
    if not CheckPost.check_format(email):
        await state.set_state(Form.post)
        await message.answer(
            f"Почта {message.text} "
            f"не соответствует формату электронного адреса, "
            f"попробуйте ввести данные еще раз"
        )
    if not CheckPost.check_domain(email, data["provider"]):
        await state.set_state(Form.post)
        await message.answer(
            f"Почта {message.text} не содержит домена {data['provider']}, возможно вы ошиблись\n\n"
            f"Попробуйте ввести почту еще раз, "
            f"либо отмените все действия нажав /cancel и "
            f"попробуйте привязать почту выбрав нужного провайдера"
        )


@router.callback_query(Text(ba.next.value), Form.check_post)
async def process_entered_password(cback: types.CallbackQuery, state: FSMContext):
    await cback.message.edit_text("Отлично! Теперь пришлите пароль для внешних приложений")
    await state.set_state(Form.password)


# TODO: валидация пароля на отсутствие стикеров,
#  файлов, смайликов, картинок и тд в сообщении
@router.message(Form.password)
async def process_passwords(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != Form.password:
        return
    await state.update_data(password=message.text)
    await message.answer(
        "Отлично! Теперь пришлите мне пароль еще раз для подтверждения",
    )
    await state.set_state(Form.check_password)
    await message.delete()


@router.callback_query(Text(ba.back.value), Form.check_post)
@router.callback_query(Text(ba.back.value), Form.check_password)
async def process_data_entered_once_more(cback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Form.check_post:
        await cback.message.edit_text("Пришлите почту еще раз!")
        await state.set_state(Form.post)
    current_state = await state.get_state()
    if current_state == Form.check_password:
        await cback.message.edit_text("Пришлите пароль еще раз!")
        await state.set_state(Form.password)


@router.message(Form.check_password)
async def process_continue_connection_choice(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != Form.check_password:
        return
    data = await state.get_data()
    password = data.get("password")
    if CheckPasswords.check_passwords(message.text, password):
        await message.answer(
            "Отлично! Подтверждаете привязку почтовых данных? \n\n"
            "Почта {email}\n"
            "Пароль <tg-spoiler>{password}</tg-spoiler>"
            "".format(**data),
            reply_markup=confirm_reset_keyboard.as_markup(),
        )
        await state.set_state(Form.connect_to_server)
        await message.delete()
    else:
        await message.answer("Введенные вами пароли не совпадают, прошу ввести пароль заново")
        await message.delete()


@router.callback_query(Text(ba.next.value), Form.connect_to_server)
async def process_check_on_server(cback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state != Form.connect_to_server:
        return

    # data = await state.get_data()
    # sender_gateway: SenderApiGateway = await get_sender_gateway()
    # await sender_gateway.create(cback.message.from_user.id, )

    # TODO: подключение к почтам через imap и проверка их на сервере
    # TODO: отсюда до очистики стейта передаем данные на запись в бд
    await state.clear()  # очистить стейт после пинга почты на сервере
    await state.set_state(None)
    # TODO: идем в апишку, пытаемся привязать почту, стучимся на imap сервер

    await cback.message.edit_text("Подтверждено! Подключение производится...")


# TODO: добавить отработку событий неуспешной привязки почты и так далее, затем закрыть состояние
