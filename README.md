# Todoist CLI
CLI app for [todoist](https://todoist.com/)

## Installation
For install this app you need [poetry](https://poetry.com/)

```sh
poetry build
```

Then:
```
pip install dist/todoist_cli-0.0.1-py3-none-any.whl
```

Also, you need to create config file - `$HOME/.todoist_cli_config.cfg`:
```
[DEFAULT]
TODOIST_API_KEY = your-api-key
```

## Usage
```sh
tdc --help
tdc get-tasks-due-today
```