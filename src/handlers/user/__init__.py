from aiogram import Router

from src.handlers.user.info import router as info_router
from src.handlers.user.password.link import router as link_router
from src.handlers.user.provider import router as provider_router
from src.handlers.user.unlink import router as unlink_router
from src.handlers.user.list import router as list_router

__all__ = ("user_router",)

user_router = Router()
list_router.include_router(unlink_router)
user_router.include_routers(provider_router, link_router, list_router)
user_router.include_routers(info_router)
