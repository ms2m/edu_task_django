# edu_task_django
<!-- Create project -->
django-admin startproject tutorials

<!-- create core app -->
cd tutorials && python manage.py startapp core

<!-- create auth app -->
python manage.py startapp accounts

<!-- Run server -->
python manage.py runserver

<!-- Make migration on changes you make to your models (adding a field, deleting a model, etc.) into your database schema. -->
python manage.py makemigrations

<!-- sync your database for the first time -->
python manage.py migrate

<!-- We'll authenticate as that user later in our example. -->
python manage.py createsuperuser --email admin@example.com --username admin
admin/admin

<!-- Created Register and login apis -->
http://127.0.01:8000/api/login/

Eg: 
{
    "username":"ms",
    "email":"abc@gmail.com",
    "password":"1234",
    "password2":"1234"
}

<!-- Login user to get access token -->
http://127.0.01:8000/api/login/

Eg:
{
    "username":"ms",
    "password": "1234"
}



