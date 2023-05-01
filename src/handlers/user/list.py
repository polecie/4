from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from src.callbacks import Pagination as pg
from src.callbacks import ShowItems as si
from src.filters.user import CheckPosts
from src.handlers.user.mock import senders, user_response
from src.keyboards import generate_enumeration_keyboard, show_keyboard
from src.states import ShowConnectedItems as Form

__all__ = ("router",)

router = Router()


@router.message(Command("show"), CheckPosts(user_response))
async def process_show_command(
    message: types.Message,
    state: FSMContext,
    status,
):
    if status:
        current_state = await state.get_state()
        if current_state is not None:
            return
        await message.answer(
            "Для того чтобы просмотреть список привязанных отправителей нажмите "
            "на кнопку Отправители, для того чтобы просмотреть список привязанных "
            "почт нажмите на кнопку Почты",
            reply_markup=show_keyboard.as_markup(),
        )
        await state.set_state(Form.show_choice)
    if status is False:
        await message.answer(
            "У вас еще нет привязанных почт, для того чтобы привязать почту нажмите на кнопку /connect, "
            "после того как произойдет привязка, вам будет доступна данная команда!"
        )


@router.callback_query(
    Text(si.posts.value),
    Form.show_choice,
)
async def process_show_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    await state.update_data(section=si.posts.value)
    keyboard = await generate_enumeration_keyboard(items=user_response)  # TODO: заменить на запрос к апишке
    await state.update_data(page=1)
    if user_response:  # TODO: заменить на запрос к апишке
        await cback.message.edit_text(
            "Для того чтобы отвязать какую-либо из ваших почт, выберите ее в списке ниже\n\n"
            "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n",
            reply_markup=keyboard.as_markup(),
        )
        await state.set_state(Form.content)


@router.callback_query(
    Text(startswith=pg.next_page.value),
    Form.content,
)
async def process_next_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    section = data.get("section")
    cback_data = cback.data
    page = int(cback_data.split("_")[1])
    message, response_body = "", []

    await state.update_data(page=page)

    if section == si.posts.value:
        response_body = user_response
        message = "какую-либо из ваших почт, выберите ее"
    if section == si.senders.value:
        response_body = senders
        message = "какой-либо из ваших отправителей, выберите его"

    keyboard = await generate_enumeration_keyboard(page=page, items=response_body)
    await cback.message.edit_text(
        "Для того чтобы отвязать {message} в списке ниже\n\n"
        "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n".format(message=message),
        reply_markup=keyboard.as_markup(),
    )


@router.callback_query(
    Text(startswith=pg.prev_page.value),
    Form.content,
)
async def process_prev_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    section = data.get("section")
    cback_data = cback.data
    page = int(cback_data.split("_")[1])
    message, response_body = "", []

    await state.update_data(page=page)

    if section == si.posts.value:
        response_body = user_response
        message = "какую-либо из ваших почт, выберите ее"
    if section == si.senders.value:
        response_body = senders
        message = "какой-либо из ваших отправителей, выберите его"

    keyboard = await generate_enumeration_keyboard(page=page, items=response_body)
    await cback.message.edit_text(
        "Для того чтобы отвязать {message} в списке ниже\n\n"
        "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n".format(message=message),
        reply_markup=keyboard.as_markup(),
    )


@router.message(Command("back"), Form.content)
async def process_back_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    if current_state == Form.content:
        await message.answer(
            "Для того чтобы просмотреть список привязанных отправителей нажмите "
            "на кнопку Отправители, для того чтобы просмотреть список привязанных "
            "почт нажмите на кнопку Почты",
            reply_markup=show_keyboard.as_markup(),
        )
        await state.set_state(Form.show_choice)
        await state.update_data(section=None)


@router.callback_query(
    Text(si.senders.value),
    Form.show_choice,
)
async def process_show_senders_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    await state.update_data(section=si.senders.value)
    keyboard = await generate_enumeration_keyboard(items=senders)
    await state.update_data(page=1)
    if senders:
        await cback.message.edit_text(
            "Для того чтобы отвязать какого-либо из ваших отправителей, выберите его в списке ниже\n\n"
            "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n",
            reply_markup=keyboard.as_markup(),
        )
        await state.set_state(Form.content)
    if not senders:
        await cback.answer(show_alert=True, text="У вас нет привязанных отправителей")
