# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
from datetime import datetime
from typing import List

import requests
from requests import Response

from .entities.task import Due, Task


class TodoistConnector:
    URL = 'https://api.todoist.com/rest/v2'
    CONFIG_PATH = '~/.todoist_cli_config.cfg'

    def __init__(self) -> None:
        self.api_key = self.__get_api_key()
        if not self.api_key:
            raise Exception('Please provide an api key!')

    def __get_api_key(self) -> str:
        _parser = ConfigParser()
        _parser.read([os.path.expanduser(self.CONFIG_PATH)])
        return _parser.get('DEFAULT', 'TODOIST_API_KEY')

    def __get(self, path: str) -> Response:
        headers = {'Authorization': f'Bearer {self.api_key}'}
        return requests.get(f"{self.URL}/{path}", headers=headers)

    def __build_task_obj(self, data: dict) -> Task:
        if due := data.get('due'):
            data['due'] = Due(**due)
        return Task(**data)

    def get_tasks(self) -> List[Task]:
        return [
            self.__build_task_obj(task) for task in self.__get('tasks').json()
        ]

    def today(self, pretty: bool = False) -> str:
        def _filter_by_date(task: Task) -> bool:
            due: Due = getattr(task, 'due')
            if due:
                if due.date == str(datetime.now().date()):
                    return True
            return False

        _tasks: list = self.get_tasks()
        _tasks.reverse()
        _filtred_tasks = list(
            filter(lambda task: _filter_by_date(task), _tasks)
        )
        return '\n'.join([str(task) for task in _filtred_tasks])
