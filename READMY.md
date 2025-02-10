# Vitaliy_Avdoshkin_CourseWork_8

# Трекер привычек

## Описание

Проект курса
В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.
Вы будете работать над SPA-приложением.
Результатом создания проекта будет бэкенд-сервер,
который возвращает клиенту JSON-структуры.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/CourseWork_8.git
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
```

5. Установите требуемые библиотеки:
````commandline
poetry add requests
poetry add python-dotenv
poetry add psycopg2
poetry add django
poetry add redis
poetry add ipython
pip install djangorestframework
pip install django-filter
pip install djangorestframework-simplejwt
pip install drf-yasg
pip install stripe
pip install celery
pip install eventlet -- только для Windows
pip install django-celery-beat
pip install redis
````

6. Инициализируйте django-проект внутри текущей директории
````
django-admin startproject config .
````


