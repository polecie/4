from aiogram import types, Router
from aiogram.filters import Text

from src.callbacks import Callbacks as cb
from src.keyboards import menu_keyboard

__all__ = ("info",)

info = Router()


@info.callback_query(Text(cb.about.value))
async def process_about(cback: types.CallbackQuery):
    await cback.message.edit_text(
        "Проект реализован в рамках прохождения стажировки в одной из айти компаний!",
        reply_markup=menu_keyboard.as_markup()
    )


@info.callback_query(Text(cb.bot.value))
async def process_bot(cback: types.CallbackQuery):
    await cback.message.edit_text(
        "Бот для получения изображений писем с электронной почты!",
        reply_markup=menu_keyboard.as_markup()
    )
