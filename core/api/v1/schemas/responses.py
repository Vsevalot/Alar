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


class DataResponse(BaseModel):
    result: list[Data]
