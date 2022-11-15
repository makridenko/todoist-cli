# -*- coding: utf-8 -*-
from dataclasses import asdict as _asdict
from typing import Type, TypeVar


_T = TypeVar('_T')


class BaseMixin:
    @classmethod
    def from_dict(cls: Type[_T], data: dict) -> _T:
        return cls(**data)

    def as_dict(self) -> dict:
        return _asdict(self)
