import aiohttp
import asyncio
from typing import TypedDict


class Data(TypedDict):
    id: int
    name: str


class DataClient:
    async def get_data(self, url: str) -> list[Data]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                return await resp.json()