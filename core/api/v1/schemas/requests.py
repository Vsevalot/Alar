from pydantic import BaseModel


class CreateUserInput(BaseModel):
    name: str
    password: str
    permission: str


class UpdateUserInput(BaseModel):
    name: str | None
    password: str | None
    permission: str | None
