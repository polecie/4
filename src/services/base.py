import logging
from httpx import AsyncClient, Headers, Response


class ApiRequests:
    async def get_request(self, url: str, headers: Headers = None) -> Response | None:
        try:
            async with AsyncClient() as client:
                response: Response = await client.get(
                    url,
                    headers=headers,
                )
                return response
        except Exception as err:
            logging.error(msg="Error when connect to API", exc_info=err)
            return None

    async def post_request(
        self, url: str, data: dict | None = None, headers: Headers = None
    ) -> Response | None:
        try:
            async with AsyncClient() as client:
                response: Response = await client.post(
                    url,
                    json=data,
                    headers=headers,
                )
                return response
        except Exception as err:
            logging.error(msg="Error when connect to API", exc_info=err)
            return None

    async def delete_request(
        self, url: str, headers: Headers = None
    ) -> Response | None:
        try:
            async with AsyncClient() as client:
                response: Response = await client.delete(
                    url,
                    headers=headers,
                )
                return response
        except Exception as err:
            logging.error(msg="Error when connect to API", exc_info=err)
            return None
