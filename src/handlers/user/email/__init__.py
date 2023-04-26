from aiogram import Router
from .password.password import *
from .provider import *
from .unlink import *

__all__ = ("connect",)

connect = Router()
connect.include_routers(provider, password, disconnect)
