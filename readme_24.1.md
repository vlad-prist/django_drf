## Старт работы

в командной строке создали директорию с названием проекта и перешли в нее
mkdir django_drf > cd django_drf

В ней же активировали вирт окружение
python -m venv venv 
venv\Scripts\activate

далее установили:
pip install django
django-admin startproject config .
pip install psycopg2-binary
pip install pillow
pip install djangorestframework

В самом PyCharm открыли новый проект, добавили в settings.py приложение rest_framework
Добавили ALLOWED_HOSTS = ['*']
Прописали настройки БД
Подключились к БД (psql -U postgres) и создали БД (create database django_drf;)

Создали приложение Users
в настройках settings.py добавили AUTH_USER_MODEL = 'users.User'
Сделали миграции


Для авторизации через JWT в DRF необходимо:
1) Установить библиотеку djangorestframework-simplejwt 
Настроить параметры в файле settings.py (например, время жизни токенов).
Создать представление (view) и сериализатор для получения токена.
Настроить маршруты для эндпоинта получения токена.
 
2) Для установки прав доступа для контроллеров в DRF нужно:
Импортировать классы разрешений из rest_framework.permissions
Установить класс разрешений в атрибуте permission_classes для контроллера (класса представления).
Помнить, что доступные классы разрешений включают AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
Создать пользовательские классы разрешений, если нужно, путем наследования от BasePermission и переопределения методов проверки прав доступа.

3) Для установки прав доступа для моделей в DRF требуется:
Установить класс разрешений в атрибуте permission_classes для сериализатора или представления (класса представления).
Помнить, что доступные классы разрешений включают DjangoModelPermissions и DjangoObjectPermissions
Создать пользовательские классы разрешений, если нужно, путем наследования от BasePermission и переопределения методов проверки прав доступа.


Подсчет покрытия тестами
Для подсчета покрытия тестами используется специальный пакет 
pip install coverage
После установки важно запустить подсчет покрытия и вывести отчет:
coverage run --source='.' manage.py test
coverage report

drf-yasg
Для установки drf-yasg - переходим на оф сайт и следуем инструкции
https://drf-yasg.readthedocs.io/en/stable/readme.html#usage
далее устанавливаем pip install setuptools

CORS
https://pypi.org/project/django-cors-headers/
Устанавливаем, через pip install
добавляем в settings.py в INSTALLED_APPS, MIDDLEWEARS, а также добавляем CORS_ALLOWED_ORIGINS, CSRF_TRUSTED_ORIGINS
]

26.2/1 Celery.
pip install celery
pip install eventlet
pip install redis
About Celery:
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
About Reddis:
https://skillbox.ru/media/base/kak_ustanovit_redis_v_os_windows_bez_ispolzovaniya_docker/?topic=base&section=kak_ustanovit_redis_v_os_windows_bez_ispolzovaniya_docker

26.2/2 В PowerShell активировали redis:
1 окно: redis-server
2 окно: redis-cli

Добавили настройки redis в settings.py
Создали задачу в tasks.py 
перенесли задачу в контроллер MilageCreateAPIView
запустили celery

Периодическую задачу можно настроить в админке, создав Periodic Tasck, в ней прописать кастомную задаяу
пример: vehicle.tasks.check_filter
выбрать Interval Schedule
Save)