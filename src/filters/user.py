import typing
from aiogram import types
from aiogram.filters import Filter


class HasConnectedE(Filter):
    """
    Фильтр для проверки наличия привязанных почт у пользователя.
    Если они есть, то проталкивает их в хэндлер.
    """
    def __init__(self, response_body: dict) -> None:
        # в списке должен содержаться айдишник tg пользователя
        self.response_body = response_body

    async def __call__(self, message: types.Message) -> dict | bool:
        # user_id = message.from_user.id
        if self.response_body["count"] != 0:
            return {"response_body": self.response_body}
            # если почты есть, то "проталкиваем" их в хэндлер по имени "emails"
        return False
