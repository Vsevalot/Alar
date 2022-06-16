from typing import TypedDict

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
