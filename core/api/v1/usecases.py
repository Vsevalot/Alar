from core.entities import Data
from core.api.v1 import repositories
from core.api.definitions import Application


async def get_healthcheck(app):
    return {'service_api': {'ok': True}}


async def get_data(app: Application) -> list[Data]:
    data = await repositories.get_data(
        client=app.data_client,
        urls=app.config.data.URLS,
    )
    return sorted(data, key=lambda d: d['id'])
