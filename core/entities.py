from typing import TypedDict
from enum import Enum

"""
In a real project it's better to use the same approach to all entities
but here I just show different definitions - with TypedDict and pure classes

Dataclasses or BaseModels aren't used intentionally
1. I already showed the usage of BaseModel in responses and requests
2. It's better to keep domain entities with the minimum amount dependencies
"""


class Data(TypedDict):
    id: int
    name: str


class Permissions(str, Enum):
    all = 'all'
    readonly = 'readonly'


class User:
    def __init__(
        self,
        id: int,
        name: str,
        permission: str,
    ):
        self.id = id
        self.name = name
        self.permission = permission
