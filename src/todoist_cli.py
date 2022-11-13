#!/bin/python3
# -*- coding: utf-8 -*-

import sys

import click

from .connectors import TodoistConnector


@click.group()
def todoist_cli():
    """A CLI wrapper for the Todoist API"""
    pass


@todoist_cli.command()
def get_tasks_due_today() -> None:
    """List of all today tasks from todoist"""
    connector = TodoistConnector()
    sys.stdout.write(connector.get_tasks_due_today() + '\n')


def main():
    todoist_cli(prog_name="todoist-cli")
