from aiogram import Router

from .base import router as base_router
from .user import user_router

__all__ = ("router",)

router = Router()
router.include_routers(base_router, user_router)
