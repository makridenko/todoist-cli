# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
from datetime import datetime
from typing import List, Optional

import requests
from requests import Response

from .entities import Due, Project, Task


class TodoistAPIWorker:
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

    def _get(self, path: str, params: Optional[dict] = None) -> Response:
        headers = {'Authorization': f'Bearer {self.api_key}'}
        return requests.get(
            f"{self.URL}/{path}",
            headers=headers,
            params=params,
        )


class TodoistObjectsWorker:
    def get_tasks(self, project_id: Optional[int] = None) -> List[Task]:
        _params = {}
        if project_id:
            _params['project_id'] = project_id

        json_tasks: list = self._get('tasks', params=_params).json()
        json_tasks.reverse()

        return [Task.from_dict(task) for task in json_tasks]

    def get_projects(self) -> List[Project]:
        json_projects = self._get('projects').json()
        return [Project.from_dict(project) for project in json_projects]

    def get_inbox_project(self) -> Project:
        return next(prj for prj in self.get_projects() if prj.is_inbox_project)


class TodoistConnector(TodoistAPIWorker, TodoistObjectsWorker):
    def today(self) -> str:
        def _filter_by_date(task: Task) -> bool:
            due: Due = getattr(task, 'due')
            if due:
                if due.date == str(datetime.now().date()):
                    return True
            return False

        _tasks: list = self.get_tasks()
        _filtred_tasks = list(
            filter(lambda task: _filter_by_date(task), _tasks)
        )
        return '\n'.join([str(task) for task in _filtred_tasks])

    def inbox(self) -> str:
        _tasks = self.get_tasks(project_id=self.get_inbox_project().id)
        return '\n'.join([str(task) for task in _tasks])
