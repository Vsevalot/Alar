from logging import Logger
import functools

from core.api import definitions
from core.settings import Config, AppConfig
from core.api.v1.routes import get_routes


def _get_app(config: AppConfig) -> definitions.Application:
    return definitions.Application(
        title=config.HTTP_API_NAME,
        description=config.HTTP_API_DESCRIPTION,
        version=config.HTTP_API_VERSION,
    )


async def _on_startup(
    application: definitions.Application,
    config: Config,
):
    application.logger = Logger(
        name=config.app.HTTP_API_NAME,
        level=config.app.LOG_LEVEL,
    )
    application.config = config


def create(config: Config) -> definitions.Application:
    app = _get_app(config.app)
    app.router.add_event_handler(
        event_type='startup',
        func=functools.partial(
            _on_startup,
            application=app,
            config=config,
        ),
    )
    for route in get_routes():
        app.router.add_api_route(**route)

    return app
