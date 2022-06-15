import fastapi
from logging import Logger
from core.settings import Config


class Application(fastapi.applications.FastAPI):
    logger: Logger
    config: Config


class Request(fastapi.Request):
    app: Application


Response = fastapi.Response
