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
