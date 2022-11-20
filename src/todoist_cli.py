#!/bin/python3
# -*- coding: utf-8 -*-

import click

from .connectors import TodoistConnector


@click.group()
def todoist_cli():
    """A CLI wrapper for the Todoist API"""
    pass


@todoist_cli.command()
@click.option(
    '-i',
    '--with-id',
    is_flag=True,
    help='Show tasks with id',
)
def today(with_id: bool) -> None:
    """List of all today tasks from todoist"""
    connector = TodoistConnector()
    click.echo(connector.today(with_id=with_id))


@todoist_cli.command()
@click.option(
    '-i',
    '--with-id',
    is_flag=True,
    help='Show tasks with id',
)
def inbox(with_id: bool) -> None:
    """List of all tasks from inbox from todoist"""
    connector = TodoistConnector()
    click.echo(connector.inbox(with_id=with_id))


@todoist_cli.command()
@click.option(
    '-c',
    '--content',
    type=str,
    required=True,
    help='Task name',
)
@click.option(
    '-p', '--priority', type=int, help='Set task priority [1(high)-4(low)]'
)
def add_inbox_task(content, priority) -> None:
    """Add task to inbox"""
    connector = TodoistConnector()
    connector.add_task_to_inbox(content, priority)


def main():
    todoist_cli(prog_name="todoist-cli")
