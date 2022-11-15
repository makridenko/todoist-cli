from typing import Type, TypeVar

_T = TypeVar('_T')


class BaseMixin:
    @classmethod
    def from_dict(cls: Type[_T], data: dict) -> _T:
        return cls(**data)
