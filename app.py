import click

from exceptions import (
    CustomGetTypeError,
    CustomListTypeError,
    CustomUnknownBuildError,
    CustomUnknownTaskError,
)
from func import get_build_tasks, get_builds, get_tasks


@click.group()
def main():
    pass


@main.command()
@click.argument("data_type")
@click.option("-p", "--path", help="Полный путь до tasks или builds")
def list(data_type, path=None):
    """
    Вывод списка tasks и builds
    """
    if data_type == "tasks":
        tasks = get_tasks(path)
        print("List of available tasks:")
        [print(f"* {task_name}") for task_name in tasks]
    elif data_type == "builds":
        builds = get_builds(path)
        print("List of available builds:")
        [print(f"* {build_name}") for build_name in builds]
    else:
        raise CustomListTypeError(
            f"Неверный data_type {data_type}, доступны tasks и builds"
        )


@main.command()
@click.argument("data_type")
@click.argument("name")
@click.option("-p", "--path", help="Полный путь до tasks или builds")
def get(data_type, name, path=None):
    """
    Вывод детальной информации о task или build
    """
    if data_type == "task":
        tasks = get_tasks(path)
        if name not in tasks:
            raise CustomUnknownTaskError(
                f"Task {name} отсутствует в tasks"
            )
        print("Task info:")
        print(f"* name: {name}")
        print(f"* dependencies: {', '.join(tasks.get(name))}")
    elif data_type == "build":
        builds = get_builds(path)
        path = path.replace("builds.yaml", "tasks.yaml") if path else None
        tasks = get_tasks(path)
        if name not in builds:
            raise CustomUnknownBuildError(
                f"Build {name} отсутствует в builds"
            )
        build_tasks = get_build_tasks(builds.get(name), tasks)
        print("Build info:")
        print(f"* name: {name}")
        print(f"* tasks: {', '.join(build_tasks)}")
    else:
        raise CustomGetTypeError(
            f"Неверный data_type {data_type}, доступны task и build"
        )


if __name__ == "__main__":
    main()
