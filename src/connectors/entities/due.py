# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional


@dataclass
class Due:
    string: str
    date: str
    is_recurring: bool
    lang: str
    datetime: Optional[str] = None
    timezone: Optional[str] = None
