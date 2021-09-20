# edu_task_django

<!-- Install requirements -->
pip install -r requirements.txt

<!-- Run server -->
python manage.py runserver

<!-- Make migration on changes you make to your models (adding a field, deleting a model, etc.) into your database schema. -->
python manage.py makemigrations

<!-- sync your database for the first time -->
python manage.py migrate

<!-- We'll authenticate as that user later in our example. -->
python manage.py createsuperuser --email admin@example.com --username admin

admin/admin


<!-- Admin -->
## View all info..
http://127.0.01:8000/admin/


<!-- Created Register and login apis -->
http://127.0.01:8000/api/login/

## Eg: 
{
    "username":"ms",
    "email":"abc@gmail.com",
    "password":"1234",
    "password2":"1234"
}

<!-- Login user to get access token. Valid for 24 hours only.-->
http://127.0.01:8000/api/login/

## Eg:
{
    "username":"ms",
    "password": "1234"
}


<!-- Course Post (Auth must required: Brearer Token: access token)--> 
http://127.0.01:8000/api/courselists/

## Eg.:
    {"title": "angular"}

<!-- Section Post (Auth must required: Brearer Token: access token)-->
http://127.0.01:8000/api/sectionlists/

## Eg.:  'course' is the id of Course api item.
{headers: {"Authorization": "Bearer  <access token>"}}
{
    "title": "Set-up angular",
    "course": 8
}


<!-- Lecture Post -->
http://127.0.01:8000/api/lecturelists/
## (Auth must required)
headers = {"Authorization": "Bearer  <access token>"}
## Eg.:  'section' is the id of Section api item.
{
    "title": "Setting up on Windows",
    "section": 4
}


<!-- Lecture Get -->
http://127.0.01:8000/api/lecturelist/<pk>
## (Auth must required)
headers = {"Authorization": "Bearer  <access token>"}
## Eg.:  'section' is the id of Section api item.
http://127.0.01:8000/api/lecturelist/11


<!-- Lecture Put -->
http://127.0.01:8000/api/lecturelist/<pk>
## (Auth must required)
headers = {"Authorization": "Bearer  <access token>"}
## Eg.:  'section' is the id of Section api item.
http://127.0.01:8000/api/lecturelist/11
{
    "title": "Setting up on mac os",
    "section": 4
}

<!-- Lecture Delete -->
http://127.0.01:8000/api/lecturelist/<pk>
## (Auth must required)
headers = {"Authorization": "Bearer  <access token>"}
## Eg.:  'section' is the id of Section api item.
http://127.0.01:8000/api/lecturelist/11







## References:

<!-- Navigate to ORM for make obj relation in serializers.py-->
cd tutorials
python manage.py shell
    from core.models import CourseList, SectionList, LectureList
    ## cl[0].checklistitem_set # created by django by reverse traverse
    cl = SectionList.objects.all()
    dir(cl[0])

    cl = CourseList.objects.all()
    dir(cl[0])

    cl = LectureList.objects.all()
    dir(cl[0])

<!-- Create project -->
django-admin startproject tutorials

<!-- create core app -->
cd tutorials && python manage.py startapp core

<!-- create auth app -->
python manage.py startapp accounts