# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

from .base import BaseMixin
from .enums import ProjectViewStyle


@dataclass
class Project(BaseMixin):
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
    view_style: ProjectViewStyle
    url: str

    def __str__(self) -> str:
        return self.name
