import fastapi
from logging import Logger
from core.settings import Config
from core.clients import DataClient


class Application(fastapi.applications.FastAPI):
    logger: Logger
    config: Config
    data_client: DataClient


class Request(fastapi.Request):
    app: Application


Response = fastapi.Response
