from enum import Enum

from aiogram.utils.keyboard import InlineKeyboardButton

from src.callbacks import About as ab
from src.callbacks import BasicActions as ba
from src.callbacks import ConnectionType as ct
from src.callbacks import Providers as ps
from src.callbacks import ShowItems as st


class BaseButtons(Enum):
    back = InlineKeyboardButton(text="Назад", callback_data=ba.back.value)
    cancel = InlineKeyboardButton(text="Отмена", callback_data=ba.cancel.value)
    next = InlineKeyboardButton(text="Далее", callback_data=ba.next.value)
    continue_ = InlineKeyboardButton(text="Продолжить", callback_data=ba.next.value)
    repeat = InlineKeyboardButton(text="Ввести еще раз", callback_data=ba.back.value)
    confirm = InlineKeyboardButton(text="Подтвердить", callback_data=ba.next.value)
    reset = InlineKeyboardButton(text="Сбросить", callback_data=ba.cancel.value)
    not_found = InlineKeyboardButton(text="Нет подходящего", callback_data=ba.not_found.value)


class MenuButtons(Enum):
    about = InlineKeyboardButton(text="О проекте", callback_data=ab.about.value)
    bot = InlineKeyboardButton(text="О боте", callback_data=ab.bot.value)


class ProviderButtons(Enum):
    gmail = InlineKeyboardButton(text=ps.gmail.value, callback_data=ps.gmail.value)
    yandex = InlineKeyboardButton(text=ps.yandex.value, callback_data=ps.yandex.value)
    mail = InlineKeyboardButton(text=ps.mail.value, callback_data=ps.mail.value)
    outlook = InlineKeyboardButton(text=ps.outlook.value, callback_data=ps.outlook.value)


class ConnectionTypeButtons(Enum):
    oauth = InlineKeyboardButton(text="Авторизоваться", callback_data=ct.oauth.value)
    password = InlineKeyboardButton(text="Пароль", callback_data=ct.password.value)


class ShowButtons(Enum):
    senders = InlineKeyboardButton(text="Отправители", callback_data=st.senders.value)
    emails = InlineKeyboardButton(text="Почты", callback_data=st.posts.value)


# class BotButtons(typing.NamedTuple):
#     text: str
#     cback_data: str
#     section: list[str] | None = None


# def create_buttons(
#         custom_button: BotButtons,
# ) -> InlineKeyboardButton:
#     button = InlineKeyboardButton(
#         text=custom_button.text,
#         callback_data=custom_button.cback_data
#     )
#     return button
