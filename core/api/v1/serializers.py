from abc import ABC, abstractmethod
from core.entities import User


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data) -> dict: ...

    @abstractmethod
    def deserialize(self, data: dict): ...


class UserSerializer(Serializer):
    @classmethod
    def serialize(cls, data: User) -> dict:
        return {'id': data.id, 'name': data.name, 'permission': data.permission}

    @classmethod
    def deserialize(cls, data: dict) -> User:
        return User(id=data['id'], name=data['name'], permission=data['permission'])
