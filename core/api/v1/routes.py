import typing
from core.api.v1 import views
from core.api.v1 import schemas


class ResponseParam(typing.TypedDict):
    model: typing.Any


class RouteParams(typing.TypedDict):
    path: str
    endpoint: typing.Callable
    responses: typing.Optional[typing.Dict[
        int | str,
        ResponseParam,
    ]]
    methods: typing.Sequence[str]


def get_routes() -> typing.Sequence[RouteParams]:
    return (
        RouteParams(
            path='/api/v1/healthcheck',
            endpoint=views.healthcheck,
            responses={
                200: ResponseParam(
                    model=schemas.responses.ServiceStatusResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
                503: ResponseParam(
                    model=schemas.responses.ServiceStatusResponse,
                ),
            },
            methods=('GET',),
        ),
        RouteParams(
            path='/api/v1/data',
            endpoint=views.data,
            responses={
                200: ResponseParam(
                    model=schemas.responses.DataResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('GET',),
        ),
    )
