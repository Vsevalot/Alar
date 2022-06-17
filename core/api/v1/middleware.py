from typing import Callable
from uuid import uuid4

from core.api.definitions import Request, Response
from core.api.v1.schemas.responses import error_response


async def logger_middleware(
        request: Request,
        call_next: Callable,
) -> Response:
    logger = request.app.logger
    trace_id = uuid4()
    logger.info(dict(
        message=f"Request path={request.url.path}",
        trace_id=trace_id,
    ))
    response = await call_next(request)
    logger.info(dict(
        message=f"Request completed",
        trace_id=trace_id,
    ))
    return response


async def exception_middleware(
    request: Request,
    call_next: Callable,
) -> Response:
    try:
        return await call_next(request)
    except Exception as e:
        request.app.logger.exception(e)
        return error_response(
            message='Internal server error',
            status=500,
        )
