from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from src.callbacks import BasicActions as ba
from src.callbacks import Providers as ps
from src.keyboards import base_keyboard, connection_type_keyboard, providers_keyboard
from src.states import ConnectionEForm as Form

__all__ = ("provider",)

provider = Router()


@provider.message(Command("connect"))
async def process_connect_command(message: types.Message, state: FSMContext):
    """Обработчик команды `/connect`. Обрабатывает событие привязки почтового
    ящика, запускает состояние привязки почты.

    :param message: Сообщение от пользователя.
    :param state: Состояние пользователя.
    :return: Возвращает пользователю клавиатуру с кнопками, которые имеют cback `next` и `cancel`.
    """
    # TODO: проверить привязана ли почта пользователя уже
    # TODO: проверка на запущенное состояние
    # TODO: удалять повторяющиеся команды или спам не соответсвующий состоянию
    current_state = await state.get_state()  # получаем текущее состояние пользователя
    if current_state is not None:  # если состояние не пустое
        return  # прерываем выполнение функции, запрещая повторную реакцию на команду `/connect`
    # TODO: вынести текстовые сообщения в шаблоны
    await message.answer(
        "Отлично! Давайте приступим к настройке бота!\n"
        "Нажмите <b>Далее</b>, если вы готовы приступить к привязке почтовых данных\n",
        reply_markup=base_keyboard.as_markup(),
    )
    await state.set_state(Form.provider)


@provider.callback_query(Text(ba.next.value), Form.provider)
async def process_connection_continued(cback: types.CallbackQuery):
    """Обработчик нажатия на кнопку `next` в состоянии подтверждения привязки
    данных.

    :param cback: CallbackQuery от пользователя.
    :return: Возвращает пользователю клавиатуру с провайдерами, а также с кнопками,
    которые имеют cback `not_found` и `back`.
    """
    await cback.message.edit_text(
        "Супер! В меню вам необходимо выбрать провайдера, "
        "к которому необходимо будет произвести подключение\n\n"
        "Если вы не нашли своего провайдера, нажмите на кнопку <b>Нет подходящего</b>\n",
        reply_markup=providers_keyboard.as_markup(),
    )


@provider.callback_query(Text(ba.back.value), Form.provider)
async def process_connection_stepped_back(cback: types.CallbackQuery, state: FSMContext):
    """Обработчик нажатия на кнопку `back` из состояния подтверждения привязки
    данных. Возвращает пользователя в главное меню.

    :param cback: CallbackQuery от пользователя.
    :param state: Состояние пользователя.
    :return: Возвращает пользователя в главное меню, возвращает клавиатуру
    с кнопками, которые имеют cback `next` и `cancel`.
    """
    await cback.message.edit_text(
        "Отлично, давайте приступим к настройке бота! "
        "Нажмите <b>Далее</b>, если готовы приступить к привязке почтовых данных\n",
        reply_markup=base_keyboard.as_markup(),
    )
    await state.set_state(Form.provider)


@provider.callback_query(Text(ps.yandex.value), Form.provider)
@provider.callback_query(Text(ps.gmail.value), Form.provider)
@provider.callback_query(Text(ps.mail.value), Form.provider)
@provider.callback_query(Text(ps.outlook.value), Form.provider)
async def process_provider(cback: types.CallbackQuery, state: FSMContext):
    """Обработчик выбора почтового провайдера для привязки почты. Обрабатывает
    для всех провайдеров в списке клавиатуры `providers_keyboard`.

    :param cback: CallbackQuery от пользователя.
    :param state: Состояние пользователя.
    :return: Возвращает пользователю клавиатуру `authentication_keyboard` + кнопку `back`.
    """
    await state.update_data(provider=cback.data)
    await cback.message.edit_text(
        f"На данный момент подключение к сервису <b>{cback.data}</b> "
        f"поддерживается через oauth2 и с помощью пароля для внешних приложений\n\n"
        "Выберите один из вариантов подключения ниже",
        reply_markup=connection_type_keyboard.as_markup(),
    )
    await state.set_state(Form.connection_type)


@provider.callback_query(Text(ba.back.value), Form.connection_type)
async def process_provider_stepped_back(cback: types.CallbackQuery, state: FSMContext):
    """Обработчик нажатия на кнопку `back` в состоянии выбора провайдера.
    Возвращает пользователя в состояние выбора провайдера.

    :param cback: CallbackQuery от пользователя.
    :param state: Состояние пользователя.
    :return: Возвращает пользователю клавиатуру с провайдерами, а также с кнопками,
    которые имеют cback `not_found` и `back`.
    """
    await cback.message.edit_text(
        "Супер! Вам необходимо выбрать провайдера, "
        "к которому необходимо будет произвести подключение\n\n"
        "Если вы не нашли своего провайдера, нажмите на кнопку <b>Нет подходящего</b>\n",
        reply_markup=providers_keyboard.as_markup(),
    )
    await state.set_state(Form.provider)
