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
            endpoint=views.get_data,
            responses={
                200: ResponseParam(
                    model=schemas.responses.DataListResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('GET',),
        ),
        RouteParams(
            path='/api/v1/users',
            endpoint=views.get_users,
            responses={
                200: ResponseParam(
                    model=schemas.responses.UserListResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('GET',),
        ),
        RouteParams(
            path='/api/v1/users',
            endpoint=views.create_user,
            responses={
                200: ResponseParam(
                    model=schemas.responses.UserResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('POST',),
        ),
        RouteParams(
            path='/api/v1/users/{user_id}',
            endpoint=views.get_user,
            responses={
                200: ResponseParam(
                    model=schemas.responses.UserResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('GET',),
        ),
        RouteParams(
            path='/api/v1/users/{user_id}',
            endpoint=views.update_user,
            responses={
                200: ResponseParam(
                    model=schemas.responses.UserMutableResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('PUT',),
        ),
        RouteParams(
            path='/api/v1/users/{user_id}',
            endpoint=views.delete_user,
            responses={
                200: ResponseParam(
                    model=schemas.responses.UserMutableResponse,
                ),
                500: ResponseParam(
                    model=schemas.responses.Error,
                ),
            },
            methods=('DELETE',),
        ),
    )
