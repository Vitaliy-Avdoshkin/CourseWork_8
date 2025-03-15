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

## Трекер привычек:

7. Создайте приложения habit и users
````
python manage.py startapp habit
python manage.py startapp users
````
2. Зарегистрируйте приложения в settings.py
3. Для приложения habit создайте моделm habit
4. Для приложения users создайте модель user
5. Опишите CRUD для всех моделей на основе ViewSet и Generic-классов
6. Создайте сериализаторы
7. Настройте права доступа
8. Опишите требуемые валидаторы
9. Добавьте пагинацию
10. Протестируйте полученный код
11. Поключите и настройте вывод документации для проекта
12. Настройте celery. Запуск селери и воркер : celery -A config worker --beat --scheduler django --loglevel=info
13. Запуск селери и воркер : celery -A config worker --beat --scheduler django --loglevel=info
14. Как запускать с докер из консоли: Ввести команду для сборки образов и запуска контейнеров: docker-compose up -d —build

## Настройка удаленного сервера
1. Сервер настроен для развертывания веб-приложения.
2. Установлены необходимые пакеты и зависимости для работы проекта (Python, Django, Gunicorn, Nginx).
3. Приложение доступно по IP-адресу сервера или домену - 158.160.91.97
4. Настроены параметры безопасности: закрыты ненужные порты, используются SSH-ключи для доступа.
5. Сервер может автоматически перезагружать приложение при внесении изменений, например с использованием Systemd или Supervisor для управления процессами.

## Шаги выполнения запуска workflow
* Файл YAML для GitHub Actions находится в репозитории в папке .github/workflows.
* Workflow запускается при каждом push в репозиторий.
* Workflow включает шаг для запуска тестов проекта.
* Тесты успешно выполняются в рамках workflow и завершаются с отчетом.
* Ошибки тестов останавливают выполнение следующих шагов workflow.
* Workflow содержит шаг деплоя, который запускается только после успешного завершения тестов.
* Проект автоматически деплоится на удаленный сервер при push, pull request
* Деплой выполняется корректно, без ошибок.


# Критерии приемки курсовой работы
## Контейнеризация
Все сервисы проекта выделены в отдельные контейнеры: Django, PostgreSQL, Redis, Celery, nginx и другие при необходимости.
Для управления контейнерами используется 
docker-compose
Созданы необходимые Dockerfile для сервисов проекта.
## CI/CD
Настроен процесс CI/CD с использованием GitHub Actions.
Включены этапы тестирования, линтинга, проверки Docker-сборки.
## Деплой на сервер
Проект автоматически развертывается на удаленном сервере через Docker Compose.
Настроено управление контейнерами для обновления сервиса при деплое.
Конфигурация деплоя описана в workflow GitHub Actions.
## Документированность
## README.md
В файле README.md:
 - подробно описаны шаги запуска проекта локально и на удаленном сервере.
 - добавлен адрес сервера с развернутым приложением.
 - включена инструкция по настройке сервера и CI/CD.
## Git и GitHub
Все изменения (workflow-файл, настройки сервера) загружены в репозиторий.
Задание сдано в виде ссылки на pull request из ветки домашней работы в ветку 
develop
В коммиты не попали игнорируемые файлы (например, .env, .idea, venv, __pycache__).
