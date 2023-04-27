from pathlib import Path

from click.testing import CliRunner

from app import list, get
import exceptions

BASE_DIR = BASE_DIR = Path(__file__).resolve().parent


def test_list_echo():
    runner = CliRunner()
    tasks_path = BASE_DIR.joinpath("test_tasks.yaml")
    result = runner.invoke(list, ["tasks", "-p", tasks_path])

    assert result.exit_code == 0
    assert result.output.startswith("List of available tasks:\n")
    assert result.output.endswith("* task_3\n")

    builds_path = BASE_DIR.joinpath("test_builds.yaml")
    result = runner.invoke(list, ["builds", "-p", builds_path])

    assert result.exit_code == 0
    assert result.output.startswith("List of available builds:\n")
    assert result.output.endswith("* build_2\n")


def test_get_echo():
    runner = CliRunner()
    tasks_path = BASE_DIR.joinpath("test_tasks.yaml")
    result = runner.invoke(get, ["task", "task_3", "-p", tasks_path])

    assert result.exit_code == 0
    assert result.output.startswith("Task info:\n")
    assert result.output.endswith("* dependencies: task_0, task_2\n")

    builds_path = BASE_DIR.joinpath("test_builds.yaml")
    result = runner.invoke(get, ["build", "build_2", "-p", builds_path])

    assert result.exit_code == 0
    assert result.output.startswith("Build info:\n")
    assert result.output.endswith("* tasks: task_0, task_1, task_2, task_3\n")


def test_list_bad_cli():
    runner = CliRunner()
    bad_data_type = "bad_type"
    tasks_path = BASE_DIR.joinpath("test_tasks.yaml")
    result = runner.invoke(list, [bad_data_type, "-p", tasks_path])

    assert result.exit_code == 1
    assert isinstance(result.exception, exceptions.CustomListTypeError)

    bad_tasks_path = BASE_DIR.joinpath("bad_path", "test_tasks.yaml")
    result = runner.invoke(list, ["tasks", "-p", bad_tasks_path])

    assert result.exit_code == 1
    assert isinstance(result.exception, exceptions.CustomFileExistsError)

    tasks_path_bad_yaml = BASE_DIR.joinpath("test_bad_tasks.yaml")
    result = runner.invoke(list, ["tasks", "-p", tasks_path_bad_yaml])

    assert result.exit_code == 1
    assert isinstance(result.exception, exceptions.CustomFileParseError)


def test_get_bad_cli():
    runner = CliRunner()
    bad_data_type = "bad_type"
    task_name = "task_2"
    tasks_path = BASE_DIR.joinpath("test_tasks.yaml")
    result = runner.invoke(get, [bad_data_type, task_name, "-p", tasks_path])

    assert result.exit_code == 1
    assert isinstance(result.exception, exceptions.CustomGetTypeError)

    bad_tasks_name = "bad_task_name"
    result = runner.invoke(get, ["task", bad_tasks_name, "-p", tasks_path])

    assert result.exit_code == 1
    assert isinstance(result.exception, exceptions.CustomUnknownTaskError)
