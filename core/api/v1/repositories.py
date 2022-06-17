import typing
from typing import Sequence
import itertools

from core.clients import DataClient, DBClient
from core.entities import Data, User
from core.api.v1.serializers import UserSerializer


async def get_data(
        client: DataClient,
        urls: Sequence[str],
) -> list[Data]:
    datas = await client.get_data(urls)
    all_data = [d.get('result', []) for d in datas]
    return list(itertools.chain(*all_data))


async def get_users(
        client: DBClient,
) -> list[User]:
    raw_users = await client.get_users()
    print(f'{raw_users = }')
    users = [UserSerializer.deserialize(u) for u in raw_users]
    return users


async def get_user(
        client: DBClient,
        user_id: int,
) -> User:
    user = await client.get_user(user_id=user_id)
    return UserSerializer.deserialize(user)


async def create_user(
        client: DBClient,
        name: str,
        hashed_password: str,
        permission: str,
) -> User:
    user = await client.create_user(name=name)
    await client.create_password(
        user_id=user['id'],
        hashed_password=hashed_password,
    )
    await client.create_permission(
        user_id=user['id'],
        permission=permission,
    )
    return UserSerializer.deserialize(user | {'permission': permission})


async def update_user(
        client: DBClient,
        user_id: int,
        name: str | None,
        hashed_password: str | None,
        permission: str | None,
) -> typing.NoReturn:
    if name:
        await client.update_user(id=user_id, name=name)
    if hashed_password:
        await client.update_password(
            user_id=user_id,
            hashed_password=hashed_password,
        )
    if permission:
        await client.update_permission(
            user_id=user_id,
            permission=permission,
        )

async def delete_user(
        client: DBClient,
        user_id: int,
) -> typing.NoReturn:
    await client.soft_delete_user(user_id=user_id)
