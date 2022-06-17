from core.api.definitions import Request, Response
from core.api.v1.schemas.responses import json_response
from core.api.v1.schemas.requests import (
    CreateUserInput,
    UpdateUserInput,
)
from core.api.v1 import usecases, serializers


async def healthcheck(request: Request) -> Response:
    status = await usecases.get_healthcheck(request.app)
    return json_response(content=status)


async def get_data(request: Request) -> Response:
    data = await usecases.get_data(request.app)
    return json_response(content=data)


#TODO: add pagination
async def get_users(request: Request) -> Response:
    users = await usecases.get_users(request.app)
    return json_response(
        content=[serializers.UserSerializer.serialize(u) for u in users],
    )


async def get_user(request: Request, user_id: int) -> Response:
    user = await usecases.get_user(request.app, user_id)
    return json_response(content=serializers.UserSerializer.serialize(user))


async def create_user(
        request: Request,
        user: CreateUserInput,
) -> Response:
    user = await usecases.create_user(request.app, user.dict())
    return json_response(content=serializers.UserSerializer.serialize(user))


async def update_user(
        request: Request,
        user_id: int,
        user: UpdateUserInput,
) -> Response:
    await usecases.update_user(request.app, user_id, user.dict())
    return json_response(content={'result': 'OK'})


async def delete_user(
        request: Request,
        user_id: int,
) -> Response:
    await usecases.delete_user(request.app, user_id)
    return json_response(content={'result': 'OK'})
