# -*- coding: utf-8 -*-

import os
import sys

import click
from dotenv import load_dotenv

from connector import TodoistConnector


load_dotenv('.env')


TODOIST_API_KEY = os.getenv('TODOIST_API_KEY')


@click.group()
def todoist_cli():
    """A CLI wrapper for the Todoist API"""
    pass


@todoist_cli.command()
def get_tasks_due_today() -> None:
    """ List of all today tasks from todoist """
    connector = TodoistConnector(api_key=TODOIST_API_KEY)
    sys.stdout.write(connector.get_tasks_due_today() + '\n')


if __name__ == "__main__":
    todoist_cli(prog_name="todoist-cli")
