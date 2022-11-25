# -*- coding: utf-8 -*-

from typing import Optional

from pydantic import BaseModel


class Due(BaseModel):
    string: str
    date: str
    is_recurring: bool
    lang: str
    datetime: Optional[str] = None
    timezone: Optional[str] = None
