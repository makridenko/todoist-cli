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
