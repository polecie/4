import typing
from aiogram import types, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from src.callbacks import Callbacks as cb
from src.filters.user import HasConnectedE
from src.states import DisconnectionEForm as Form

__all__ = ("disconnect",)

disconnect = Router()

# TODO: получаем список привязанных почт пользователя из апишки в формате json с пагинацией
user_response = {
    "count": 1023,
    "next": "https://api.example.org/persons/?page=2&per_page=10",
    "previous": None,
    "results": [
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
        {"email": "example@gmail.com", "provider": "gmail", "cback_data": "gmail", "user": 537949371},
        {"email": "example2@mail.ru", "provider": "mail", "cback_data": "mail", "user": 537949371},
        {"email": "example3@yandex.com", "provider": "yandex", "cback_data": "yandex", "user": 537949371},
    ]
}

@disconnect.message(
    Command("disconnect"),
    HasConnectedE(user_response),
)
async def process_connect_command(
        message: types.Message,
        state: FSMContext,
        response_body,
):
    """
    Обработчик команды `/disconnect`. Отрабатывает только в том случае, если у пользователя есть привязанные почты.
    Обрабатывает событие отвязки почтового ящика, запускает состояние отвязки почты.
    Показывает пользователю список его привязанных почт, которые он может отвязать.

    :param message: Сообщение от пользователя.
    :param state: Состояние пользователя.

    :return: Возвращает пользователю клавиатуру с кнопками его привязанных почт.
    """
    current_state = await state.get_state()  # получаем текущее состояние пользователя
    if current_state is not None:  # если состояние не пустое
        return  # прерываем выполнение функции, запрещая повторную реакцию на команду `/disconnect`
    # TODO: вынести текстовые сообщения в шаблоны
    if response_body:
        await message.answer(
            "Для того чтобы отвязать какую-либо из ваших почт, выберите ее в списке ниже\n"
            f"Список ваших привязанных почт {response_body}",
            # reply_markup=builder.as_markup()
        )
        # await state.set_state()
