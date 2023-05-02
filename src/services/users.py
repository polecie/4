from src.services.base import ApiRequests
from src.services.responses import Responses as status

__all__ = ("UserApiGateway", "get_user_gateway")


class UserApiGateway(ApiRequests):
    def __init__(self, resource: str = "users"):
        self.resource = "http://localhost:8000/api/v1/" + resource + "/{user_id}"

    async def get(self, user_id: int) -> bool | None:
        response = await self.get_request(self.resource.format(user_id=user_id))
        if response.status_code not in (status.OK,):
            return True
        return None

    async def create(self, user_id: int) -> bool | None:
        user_data = {"id": user_id}
        response = await self.post_request(self.resource.format(user_id=""), data=user_data)
        if response.status_code == (status.CREATED, status.OK):
            # TODO: новый пользователь, или уже существующий
            return True
        return None


async def get_user_gateway() -> UserApiGateway:
    return UserApiGateway()


async def main():
    pass


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

