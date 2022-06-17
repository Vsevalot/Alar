import fastapi
from logging import Logger
from core.settings import Config
from core.clients import DataClient, DBClient


class Application(fastapi.applications.FastAPI):
    logger: Logger
    config: Config
    data_client: DataClient
    db_client: DBClient


class Request(fastapi.Request):
    app: Application


Response = fastapi.Response
