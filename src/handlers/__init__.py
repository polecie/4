from aiogram import Router

from .base import router
from .user import user as us

__all__ = ("main_router",)

main_router = Router()

main_router.include_routers(router, us)
