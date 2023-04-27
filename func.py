from pathlib import Path

import yaml

from exceptions import (
    CustomFileExistsError,
    CustomFileParseError,
    CustomUnknownTaskError,
)

BASE_DIR = Path(__file__).resolve().parent


def get_tasks(path: str) -> dict[str: list[str]]:
    """
    Парсинг tasks в словарь, формат {name: dependencies}
    """
    path = path or BASE_DIR.joinpath("tasks.yaml")
    if not Path(path).is_file():
        raise CustomFileExistsError(f"Проверьте путь до файла с tasks: {path}")

    tasks = {}
    try:
        with open(path) as f:
            data = yaml.safe_load(f)["tasks"]
            for task in data:
                name = task["name"]
                dependencies = task["dependencies"]
                tasks[name] = dependencies
    except Exception as err:
        raise CustomFileParseError(f"Ошибка извлечения данных: {err}")
    else:
        return tasks


def get_builds(path: str) -> dict[str: list[str]]:
    """
    Парсинг builds в словарь, формат {name: tasks}
    """
    path = path or BASE_DIR.joinpath("builds.yaml")
    if not Path(path).is_file():
        raise CustomFileExistsError(
            f"Проверьте путь до файла с builds: {path}"
        )

    builds = {}
    try:
        with open(path) as f:
            data = yaml.safe_load(f)["builds"]
            for build in data:
                name = build["name"]
                tasks = build["tasks"]
                builds[name] = tasks
    except Exception as err:
        raise CustomFileParseError(f"Ошибка извлечения данных: {err}")
    else:
        return builds


def get_build_tasks(
    tasks_list: list[str], tasks: dict[str: list[str]], queue: list[str] = []
) -> list[str]:
    """
    Извлечение упорядоченной очереди задач для build
    """
    for task in tasks_list:
        if task in queue:
            continue
        if task not in tasks:
            raise CustomUnknownTaskError(
                f"Task {task} отсутствует в tasks, проверьте переданный build"
            )
        dependencies = tasks.get(task)
        if dependencies:
            get_build_tasks(dependencies, tasks, queue)
        queue.append(task)
    return queue
