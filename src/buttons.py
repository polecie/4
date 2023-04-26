from enum import Enum
from aiogram.utils.keyboard import InlineKeyboardButton

from src.callbacks import Callbacks as cb


class BaseButtons(Enum):
    back = InlineKeyboardButton(text="Назад", callback_data=cb.back.value)
    cancel = InlineKeyboardButton(text="Отмена", callback_data=cb.cancel.value)
    next = InlineKeyboardButton(text="Далее", callback_data=cb.next.value)
    continue_ = InlineKeyboardButton(text="Продолжить", callback_data=cb.next.value)
    repeat = InlineKeyboardButton(text="Ввести еще раз", callback_data=cb.back.value)
    confirm = InlineKeyboardButton(text="Подтвердить", callback_data=cb.next.value)
    reset = InlineKeyboardButton(text="Сбросить", callback_data=cb.cancel.value)
    not_found = InlineKeyboardButton(text="Нет подходящего", callback_data=cb.not_found.value)


class MenuButtons(Enum):
    about = InlineKeyboardButton(text="О проекте", callback_data=cb.about.value)
    bot = InlineKeyboardButton(text="О боте", callback_data=cb.bot.value)


class ProviderButtons(Enum):
    # TODO: стоит этот список брать из базы данных или из конфига
    gmail = InlineKeyboardButton(text="gmail", callback_data=cb.gmail.value)
    yandex = InlineKeyboardButton(text="yandex", callback_data=cb.yandex.value)
    mail = InlineKeyboardButton(text="mail", callback_data=cb.mail.value)
    outlook = InlineKeyboardButton(text="outlook", callback_data=cb.outlook.value)
    # yahoo = InlineKeyboardButton(text="yahoo", callback_data=cb.yahoo.value)
    # rambler = InlineKeyboardButton(text="rambler", callback_data=cb.rambler.value)


class ConnectionTypeButtons(Enum):
    oauth = InlineKeyboardButton(text="Авторизоваться", callback_data=cb.oauth.value)
    password = InlineKeyboardButton(text="Пароль", callback_data=cb.password.value)


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
