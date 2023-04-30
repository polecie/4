from aiogram import Router
from .password.link import password as pswd
from .provider import provider as prd
from .unlink import disconnect_data
from .list import enum_data

__all__ = ("connect",)

connect = Router()
enum_data.include_router(disconnect_data)
connect.include_routers(prd, pswd, enum_data)
