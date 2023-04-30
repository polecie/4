from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from src.buttons import (
    BaseButtons,
    ConnectionTypeButtons,
    MenuButtons,
    ProviderButtons,
    ShowButtons,
)
from src.callbacks import DisconnectItem
from src.callbacks import Pagination as pg

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

show_keyboard = InlineKeyboardBuilder()
show_keyboard.add(ShowButtons.senders.value)
show_keyboard.add(ShowButtons.emails.value)
show_keyboard.add(BaseButtons.cancel.value)
show_keyboard.adjust(2, 1)

disconnect_keyboard = InlineKeyboardBuilder()
disconnect_keyboard.add(BaseButtons.confirm.value)
disconnect_keyboard.add(BaseButtons.back.value)


async def generate_enumeration_keyboard(
    # TODO: вынести эту дата в настройки
    items: list,
    page: int = 1,
    page_size: int = 3,
) -> InlineKeyboardBuilder:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    keyboard = InlineKeyboardBuilder()

    previous_button = InlineKeyboardButton(text="Назад", callback_data=f"{pg.prev_page.value}{page - 1}")
    next_button = InlineKeyboardButton(text="Далее", callback_data=f"{pg.next_page.value}{page + 1}")

    for item in items[start_index:end_index]:
        cb_data = DisconnectItem(data=item["email"])
        button = InlineKeyboardButton(text=item["email"], callback_data=cb_data.pack())
        keyboard.add(button)
    if end_index < len(items) and start_index == 0:
        keyboard.row(next_button)
    if start_index > 0 and end_index < len(items):
        keyboard.row(previous_button)
        keyboard.add(next_button)
        keyboard.adjust(3, 2)
    if end_index >= len(items) and start_index > 0:
        keyboard.row(previous_button)
    return keyboard
