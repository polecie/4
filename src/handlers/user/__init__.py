from aiogram import Router

from src.handlers.user.info import info as nf
from src.handlers.user.data import connect as cn

__all__ = ("user",)

user = Router()
user.include_routers(nf, cn)
