# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

import requests
from requests import Response

from entities.task import Due, Task


class TodoistConnector:
    URL = " https://api.todoist.com/rest/v2"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def __get(self, path: str) -> Response:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        return requests.get(f"{self.URL}/{path}", headers=headers)

    def __build_task_obj(self, data: dict) -> Task:
        if due := data.get("due"):
            data["due"] = Due(**due)
        return Task(**data)

    def get_tasks(self) -> List[Task]:
        return [
            self.__build_task_obj(task) for task in self.__get("tasks").json()
        ]

    def get_tasks_due_today(self) -> str:
        def _filter_by_date(task: Task) -> bool:
            due: Due = getattr(task, "due")
            if due:
                if due.date == str(datetime.now().date()):
                    return True
            return False

        _tasks: list = self.get_tasks()
        _filtred_tasks = list(
            filter(lambda task: _filter_by_date(task), _tasks)
        )
        return '\n'.join([task.content for task in _filtred_tasks])
