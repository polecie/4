from aiogram import types
from aiogram.filters import Filter


class CheckPosts(Filter):
    def __init__(self, status: list) -> None:
        self.status = status

    async def __call__(self, message: types.Message):
        if len(self.status) > 0:
            return {"status": True}
        return {"status": False}
