# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List, Optional

from .due import Due


@dataclass
class Task:
    id: int
    project_id: int
    content: str
    description: str
    is_completed: bool
    order: int
    priority: int
    url: str
    comment_count: int
    created_at: str
    creator_id: int
    due: Optional[Due] = None
    parent_id: Optional[int] = None
    labels: Optional[List[str]] = None
    section_id: Optional[int] = None
    assignee_id: Optional[int] = None
    assigner_id: Optional[int] = None

    priority_colors = {
        1: '\033[97m {}\033[00m',
        2: '\033[96m {}\033[00m',
        3: '\033[93m {}\033[00m',
        4: '\033[91m {}\033[00m',
    }

    def __str__(self) -> str:
        _content = f'- [] {self.content}'
        return self.priority_colors.get(self.priority).format(_content)
