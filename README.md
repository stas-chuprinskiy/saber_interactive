# Тестовое задание Saber Interactive

CLI-утилита для определения последовательности выполнения задач в билде.

### Технологии

* Python 3.10
* PyYAML==6.0
* click==8.1.3
* pytest==7.3.1

### Список доступных команд

* **list** [args] DATA_TYPE [opt] -p --path - вывод списка tasks или builds;
* **get** [args] DATA_TYPE NAME [opt] -p --path - вывод детальной информации о task или build.

### Установка

- Клонируйте репозиторий:
```
git clone <link>
```

- В файле проекта создайте виртуальное окружение:
```
python -m venv venv
```

- Установите зависимости:
```
pip install -r requirements.txt
```

### Использование

В приведенных примерах предполагается, что файлы `tasks.yaml` и `builds.yaml` расположены в корне проекта. Для смены расположения файлов запускайте cli команды с опцией -p *some_path/file.yaml*.

Получить список tasks:
```
python app.py list tasks


# Вывод
List of available tasks:
* bring_black_leprechauns
* bring_gray_cyclops
...
```

Получить список builds:
```
python app.py list builds

# Вывод
List of available builds:
* approach_important
* audience_stand
* time_alone
```

Получить информацию о task `create_green_cyclops`:
```
python app.py get task create_green_cyclops

# Вывод
Task info:
* name: create_green_cyclops
* dependencies: bring_green_cyclops, design_silver_cyclops, enable_yellow_cyclops, read_aqua_cyclops, train_white_cyclops
```

Получить информацию о build `time_alone`:
```
python app.py get build time_alone

# Вывод
Build info:
* name: time_alone
* tasks: bring_gray_cyclops, enable_white_cyclops, read_lime_cyclops, coloring_green_cyclops, bring_green_cyclops, ...
```

### Тестирование

Для запуска тестов в папке проекта выполните:

```
pytest .
```

### Автор

*Чупринский Станислав*
