from enum import Enum

from aiogram.filters.callback_data import CallbackData


class About(Enum):
    about = "about"
    bot = "bot"


class BasicActions(Enum):
    back = "back"
    next = "next"
    cancel = "cancel"
    not_found = "not_found"


class Providers(Enum):
    # TODO: брать список из базы данных или из конфига
    gmail = "gmail"
    yandex = "yandex"
    mail = "mail"
    outlook = "outlook"


class ConnectionType(Enum):
    password = "password"
    oauth = "oauth"


class ShowItems(Enum):
    senders = "senders"
    posts = "posts"


class Pagination(Enum):
    next_page = "nextpage_"
    prev_page = "prevpage_"


class Disconnect(Enum):
    prefix = "disconnect_"


class DisconnectItem(CallbackData, prefix=Disconnect.prefix.value):  # type: ignore
    """"""

    data: str
