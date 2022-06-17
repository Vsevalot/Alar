import hashlib
import typing

from core.entities import Data, User
from core.api.v1 import repositories
from core.api.definitions import Application


async def get_healthcheck(app):
    return {'service_api': {'ok': True}}


async def get_data(app: Application) -> list[Data]:
    data = await repositories.get_data(
        client=app.data_client,
        urls=app.config.data.URLS,
    )
    return sorted(data, key=lambda d: d['id'])


async def get_users(app: Application) -> list[User]:
    data = await repositories.get_users(
        client=app.db_client,
    )
    return data


async def get_user(app: Application, user_id: int) -> User:
    user = await repositories.get_user(
        client=app.db_client,
        user_id=user_id,
    )
    return user


async def create_user(
        app: Application,
        user_data: dict,
) -> User:
    hashed_password = _hash_password(
        password=user_data['password'],
        salt=app.config.auth.SERVICE_SECRET,
    )
    user = await repositories.create_user(
        client=app.db_client,
        name=user_data['name'],
        hashed_password=hashed_password,
        permission=user_data['permission'],
    )
    return user


def _hash_password(password: str, salt: str) -> str:
    password_with_salt = f'{password}{salt}'
    hashed = hashlib.sha256(password_with_salt.encode('utf-8')).hexdigest()
    return hashed


async def update_user(
        app: Application,
        user_id: int,
        user_data: dict,
) -> typing.NoReturn:
    hashed_password = None
    if 'password' in user_data:
        hashed_password = _hash_password(
            password=user_data['password'],
            salt=app.config.auth.SERVICE_SECRET,
        )
    await repositories.update_user(
        client=app.db_client,
        user_id=user_id,
        name=user_data['name'],
        hashed_password=hashed_password,
        permission=user_data['permission'],
    )


async def delete_user(
        app: Application,
        user_id: int,
) -> typing.NoReturn:
    await repositories.delete_user(
        client=app.db_client,
        user_id=user_id,
    )
