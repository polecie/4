from src.services.base import ApiRequests
from src.services.responses import Responses as status

__all__ = ("SenderApiGateway", "get_sender_gateway")


class SenderApiGateway(ApiRequests):
    def __init__(self,) -> None:
        self.resource = "http://localhost:8000/api/v1/users/{user_id}/senders/{sender_id}"

    async def create(self, user_id: int, email: str) -> bool | None:
        user_data = {"email": email}
        response = await self.post_request(self.resource.format(user_id=user_id, sender_id=""), data=user_data)
        if response.status_code == (status.CREATED, status.OK):
            # TODO: новый пользователь, или уже существующий
            return True
        return None


async def get_sender_gateway() -> SenderApiGateway:
    return SenderApiGateway()


async def main():
    pass


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
