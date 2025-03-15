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
python manage.py startapp lms
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

## Запуск локально
1. Клонируйте репозиторий
2. Создайте и заполните файл .env согласно шаблону .env.example
3. Соберите и запустите контейнеры
4. ```
   docker-compose up --build
   ```
5. Примените миграции. Откройте новый терминал (или командную строку) и выполните:
```
docker-compose exec web python manage.py migrate
```
6. Создайте суперпользователя (опционально):
```
docker-compose exec web python manage.py createsuperuser
```
Теперь проект должен быть доступен по адресу http://localhost:8000/

## Настройка удаленного сервера
1. Сервер настроен для развертывания веб-приложения.
2. Установлены необходимые пакеты и зависимости для работы проекта (Python, Django, Gunicorn, Nginx).
3. Приложение доступно по IP-адресу сервера или домену - http://158.160.91.97
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
- Настроили CORS.
- Настроили интеграцию с Телеграмом.
- Реализовали пагинацию.
- Использовали переменные окружения.
- Все необходимые модели описаны или переопределены.
- Все необходимые эндпоинты реализовали.
- Настроили все необходимые валидаторы.
- Описанные права доступа заложены.
- Настроили отложенную задачу через Celery.
- Проект покрыли тестами как минимум на 80%.
- Код оформили в соответствии с лучшими практиками.
- Имеется список зависимостей.
- Результат проверки Flake8 равен 100%, при исключении миграций.
- Решение выложили на GitHub.
