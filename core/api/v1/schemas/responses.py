import typing
import fastapi
from pydantic import BaseModel


def json_response(
    content: typing.Any = None,
    status_code: int = 200,
) -> fastapi.responses.ORJSONResponse:
    return fastapi.responses.ORJSONResponse(
        status_code=status_code,
        content=content,
    )


def error_response(
        message: str,
        status: int = 404,
) -> fastapi.responses.ORJSONResponse:
    return json_response(
        content=message,
        status_code=status,
    )


class Status(BaseModel):
    ok: bool
    details: typing.Optional[str]


class ServiceStatusResponse(BaseModel):
    service_api: Status


class Error(BaseModel):
    message: str
    code: str


class ErrorResponse(BaseModel):
    error: Error


class Data(BaseModel):
    id: int
    name: str


class DataListResponse(BaseModel):
    result: list[Data]


class User(BaseModel):
    id: int
    name: str
    permission: str


class UserResponse(BaseModel):
    result: User


class UserListResponse(BaseModel):
    result: list[User]


class UserMutableResponse(BaseModel):
    result: str
