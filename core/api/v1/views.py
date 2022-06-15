from core.api.definitions import Request, Response
from core.api.v1.schemas.responses import json_response
from core.api.v1 import usecases


async def healthcheck(request: Request) -> Response:
    request.app.logger.info(dict(
        message="Healthcheck",
    ))
    status = await usecases.get_healthcheck(request.app)
    return json_response(content=status)


async def data(request: Request) -> Response:
    request.app.logger.info(dict(
        message="Collecting data",
    ))
    data = await usecases.get_data(request.app)
    return json_response(content=data)
