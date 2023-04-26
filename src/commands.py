import typing

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

__all__ = ("setup_commands",)


class CustomBotCommand(typing.NamedTuple):
    command: str
    description: str
    extra: str


bot_commands = [
    CustomBotCommand("start", "Начать работу с ботом", "Хорошая команда, чтобы начать работу с ботом"),
    CustomBotCommand("connect", "Привязать почтовые данные", "Отслеживать почту"),

    # TODO: показывать пользователю и сделать активной в случае если привязана хоть одна почта
    CustomBotCommand("disconnect", "Отвязать почтовые данные", "Отвязать почтовые данные"),
]


async def setup_commands(bot: Bot):
    commands = []
    for command in bot_commands:
        commands.append(BotCommand(
            command=command.command,
            description=command.description))
    await bot.set_my_commands(commands, BotCommandScopeDefault(), )
