from aiogram import Router

from src.handlers.user.info import *
from src.handlers.user.email import *

__all__ = ("user",)

user = Router()
user.include_routers(info, connect)
