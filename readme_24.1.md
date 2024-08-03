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