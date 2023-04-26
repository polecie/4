from aiogram import Bot, Router, types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.filters import Text
from aiogram.methods.send_chat_action import SendChatAction
# from aiogram.utils.keyboard import InlineKeyboardButton

from src.commands import setup_commands
from src.core import settings
from src.callbacks import Callbacks as cb
# from src.filters.user import HasConnectedE
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
async def cancel(
        message: types.Message,
        state: FSMContext
):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Действие прервано! Для привязки данных жми /connect")


@router.callback_query(Text(cb.cancel.value))
async def cancel(
        cback: types.CallbackQuery,
        state: FSMContext
):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await cback.message.answer("Действие прервано! Для привязки данных жми /connect")


@router.message(
    Command("start"),
    # HasConnectedE(user_response)
)
async def start(message: types.Message, state: FSMContext,
                # response_body
                ) -> None:
    # TODO: проверить есть ли пользователь в базе данных,
    #  отдавать сообщение по наличию данных в базе
    current_state = await state.get_state()
    if current_state is not None:
        return
    # if response_body["count"] > 0:
    #     menu_keyboard.add(InlineKeyboardButton(text="Отвязать почтовые данные", callback_data=cb.back.value))
    #     menu_keyboard.adjust(2, 2)
    #     await message.answer(
    #         "Привет! 🤖 Я бот, который поможет с отслеживанием писем с электронной почты\n"
    #         "Для начала работы нажмите на /connect",
    #         reply_markup=menu_keyboard.as_markup()
    #     )
    #     return
    await message.answer(
        "Привет! 🤖 Я бот, который поможет с отслеживанием писем с электронной почты\n"
        "Для начала работы нажмите на /connect",
        reply_markup=menu_keyboard.as_markup()
    )

# TODO: если пользователь очищает чат то стейт обнуляется
