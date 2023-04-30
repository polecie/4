import asyncio

from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from src.callbacks import BasicActions as ba
from src.callbacks import Disconnect as dc
from src.callbacks import ShowItems as si
from src.handlers.user.data.mock import senders, user_response
from src.keyboards import disconnect_keyboard, generate_enumeration_keyboard, show_keyboard
from src.states import ShowConnectedItems as Form
from src.utils import get_current_state

__all__ = ("disconnect_data",)

disconnect_data = Router()


@disconnect_data.callback_query(
    Text(startswith=dc.prefix.value),
    Form.content,
)
@get_current_state
async def process_item_chosen_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    await state.set_state(Form.choose_item)
    cback_data = cback.data.split(":")[-1]
    await cback.message.edit_text(
        f"Вы действительно хотите отвязать почту <tg-spoiler>{cback_data}</tg-spoiler> от бота?\n",
        reply_markup=disconnect_keyboard.as_markup(),
    )
    await state.update_data(email=cback_data)


@disconnect_data.callback_query(
    Text(ba.next.value),
    Form.choose_item,
)
@get_current_state
async def process_disconnect_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    email, section, page = data.get("email"), data.get("section"), data.get("page")
    message, response_body = "", []

    if section == si.posts.value:
        response_body = user_response
        message = "какую-либо из ваших почт, выберите ее"
        user_response.pop(0)  # TODO: заменить на запрос к апишке
    if section == si.senders.value:
        response_body = senders
        message = "какой-либо из ваших отправителей, выберите его"
        senders.pop(0)  # TODO: заменить на запрос к апишке

    keyboard = await generate_enumeration_keyboard(items=response_body, page=page)

    if section == si.senders.value:
        if len(senders) == 0:  # TODO: заменить на полученные имаилз из апишки
            await asyncio.sleep(0.5)
            await cback.answer(show_alert=True, text=f"Ваша почта {email} успешно отвязана!")
            await cback.message.answer("Вы отвязали все подключенные отправители!")
            await asyncio.sleep(0.5)
            await cback.message.edit_text(
                "Для того чтобы просмотреть список привязанных отправителей нажмите "
                "на кнопку Отправители, для того чтобы просмотреть список привязанных "
                "почт нажмите на кнопку Почты",
                reply_markup=show_keyboard.as_markup()
            )
            await state.set_state(Form.show_choice)

    if section == si.posts.value:
        if len(user_response) == 0:  # TODO: заменить на полученные имаилз из апишки
            await asyncio.sleep(0.5)
            await cback.answer(show_alert=True, text=f"Ваша почта {email} успешно отвязана!")
            await cback.message.answer("Вы отвязали все подключенные почты!")
            await state.set_state(None)
            await cback.message.delete()

        if len(user_response) > 0:  # TODO: заменить на полученные имаилз из апишки
            await cback.answer(show_alert=True, text=f"Ваша почта {email} успешно отвязана!")
            await cback.message.edit_text(
                "Для того чтобы отвязать {message} в списке ниже\n\n"
                "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n".format(message=message),
                reply_markup=keyboard.as_markup(),
            )
            await state.update_data(email=None)
            await state.set_state(Form.content)


@disconnect_data.callback_query(
    Text(ba.back.value),
    Form.choose_item,
)
@get_current_state
async def process_back_to_choice_options_button(
    cback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    section, page = data.get("section"), data.get("page")
    message, response_body = "", []

    if section == si.posts.value:
        response_body = user_response
        message = "какую-либо из ваших почт, выберите ее"
    if section == si.senders.value:
        response_body = senders
        message = "какой-либо из ваших отправителей, выберите его"

    keyboard = await generate_enumeration_keyboard(items=response_body, page=page)

    await cback.message.edit_text(
        "Для того чтобы отвязать {message} в списке ниже\n\n"
        "Если вы хотите вернуться в меню выбора, нажмите на кнопку /back\n".format(message=message),
        reply_markup=keyboard.as_markup(),
    )
    await state.update_data(email=None)
    await state.set_state(Form.content)
