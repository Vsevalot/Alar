import aiohttp
import asyncio
from typing import Sequence


class DataClient:
    def __init__(
            self,
            get_data_endpoint: str = '/data',
            timeout: int  = 2,
    ):
        self._get_data_endpoint = get_data_endpoint
        self._session_timeout = aiohttp.ClientTimeout(
            total=None,
            sock_connect=timeout,
            sock_read=timeout,
        )

    async def get_data(self, urls: Sequence[str]) -> list[dict]:
        async with aiohttp.ClientSession(
                timeout=self._session_timeout) as session:
            tasks = [self._request_data(
                session=session,
                url=f'{url}{self._get_data_endpoint}',
            ) for url in urls]
            result = await asyncio.gather(*tasks)
            return result

    """
    It's better to use something like backoff to handle exceptions

    Segregate retryable and not retryable client errors

    But because of the requirements to the task I decided to keep things as
    simple as possible
    """
    async def _request_data(
            self,
            session: aiohttp.ClientSession,
            url: str,
    ) -> dict:
        try:
            async with session.get(url) as response:
                if response.ok:
                    return await response.json()
                return {}
        except aiohttp.ClientError:
            return {}
