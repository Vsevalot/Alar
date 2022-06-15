import asyncio
import aiohttp
import itertools


from core.api.definitions import Application


async def get_healthcheck(app):
    return {'service_api': {'ok': True}}



async def request(session, url) -> dict:
    async with session.get(url) as response:
        return await response.json()


def arrange_data(datas: list[dict]) -> list[dict]:
    all_data = [d['result'] for d in datas]
    print(f'\n{all_data = }')
    data = itertools.chain(*all_data)
    print(f'\n{data = }')
    return sorted(data, key=lambda d: d['id'])


async def get_data(app: Application):
    async with aiohttp.ClientSession() as session:
        tasks = [request(session, url) for url in app.config.data.URLS]
        result = await asyncio.gather(*tasks)
    data = arrange_data(result)
    return data
