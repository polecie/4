from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.buttons import (
    MenuButtons,
    BaseButtons,
    ProviderButtons,
    ConnectionTypeButtons,
)

menu_keyboard = InlineKeyboardBuilder()
menu_keyboard.add(MenuButtons.about.value)
menu_keyboard.add(MenuButtons.bot.value)

base_keyboard = InlineKeyboardBuilder()
base_keyboard.add(BaseButtons.next.value)
base_keyboard.add(BaseButtons.cancel.value)

providers_keyboard = InlineKeyboardBuilder()
providers_keyboard.add(ProviderButtons.gmail.value)
providers_keyboard.add(ProviderButtons.yandex.value)
providers_keyboard.add(ProviderButtons.mail.value)
providers_keyboard.add(ProviderButtons.outlook.value)
providers_keyboard.add(BaseButtons.not_found.value)
providers_keyboard.add(BaseButtons.back.value)
providers_keyboard.adjust(2, 2, 1)

connection_type_keyboard = InlineKeyboardBuilder()
connection_type_keyboard.add(ConnectionTypeButtons.oauth.value)
connection_type_keyboard.add(ConnectionTypeButtons.password.value)
connection_type_keyboard.add(BaseButtons.back.value)
connection_type_keyboard.adjust(2, 2, 1)

continue_repeat_keyboard = InlineKeyboardBuilder()
continue_repeat_keyboard.add(BaseButtons.continue_.value)
continue_repeat_keyboard.add(BaseButtons.repeat.value)

confirm_reset_keyboard = InlineKeyboardBuilder()
confirm_reset_keyboard.add(BaseButtons.confirm.value)
confirm_reset_keyboard.add(BaseButtons.reset.value)
