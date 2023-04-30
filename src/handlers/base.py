from aiogram import Bot, Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from src.callbacks import BasicActions as ba
from src.commands import setup_commands
from src.core import settings
from src.keyboards import menu_keyboard

__all__ = ("router",)

router = Router()


@router.startup()
async def startup(bot: Bot):
    await setup_commands(bot)
    await bot.send_message(settings.bot.admin_id, text="Бот запущен!")


@router.shutdown()
async def shutdown(bot: Bot):
    await bot.send_message(settings.bot.admin_id, text="Бот остановлен!")


@router.message(Command("cancel"))
async def process_cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Действие прервано! Для привязки данных жми /connect")


@router.callback_query(Text(ba.cancel.value))  # type: ignore
async def process_cancel_button(cback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await cback.message.answer("Действие прервано! Для привязки данных жми /connect")


@router.message(
    Command("start"),
)
async def start(message: types.Message, state: FSMContext) -> None:
    # TODO: проверить есть ли пользователь в базе данных,
    #  отдавать сообщение по наличию данных в базе
    current_state = await state.get_state()
    if current_state is not None:
        return
    await message.answer(
        "Привет! 🤖 Я бот, который поможет с отслеживанием писем с электронной почты\n"
        "Для начала работы нажмите на /connect",
        reply_markup=menu_keyboard.as_markup(),
    )


# TODO: если пользователь очищает чат то стейт обнуляется
