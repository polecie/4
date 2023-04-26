from enum import Enum


class Callbacks(Enum):
    about = 'about'
    bot = 'bot'

    # basic actions callbacks
    back = "back"
    next = 'next'
    cancel = 'cancel'
    not_found = 'not_found'

    # providers callbacks
    gmail = 'gmail'
    yandex = 'yandex'
    mail = 'mail'
    outlook = 'outlook'
    # yahoo = 'yahoo'
    # rambler = 'rambler'

    # connection server authorization type callbacks
    password = 'password'
    oauth = 'oauth'
