# -*- coding: utf-8 -*-

from typing import Literal, Optional

from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    color: str
    parent_id: Optional[int]
    order: int
    comment_count: int
    is_shared: bool
    is_favorite: bool
    is_inbox_project: bool
    is_team_inbox: bool
    view_style: Literal['list', 'board']
    url: str

    def __str__(self) -> str:
        return self.name
