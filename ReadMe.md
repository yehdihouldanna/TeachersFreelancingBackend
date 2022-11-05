# Teacher Freelance

This 'backend' includes API and an amdin page, it is made in duality with another project called Teacher Freelance Mobile,

Both repositories serve to develop an application that aids students and schools to find teachers for their lessons,


# List of available APIs: 

The list of all the available API could be checked with swagger at :
[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)

To update the schema after each new api :
`$ python manage.py spectacular --file schema.yml`

don't forget to check the port and host url and then add `/api/schema/swagger-ui` to acess the swagger listing all available APIs in the backend,
An api for account creation,
An api for account edit
An api for listview 

*Note* : The logout functionality requires the client (mobile to delete it's store token)


# Local postgres configuration : 
username = postgres
password = postgres


## Login details : 
The backend supports login with phone number, username and email,
any of the three can be sent in the username attribute of the request 
and the backend will check, if that username is either,
and authenticate the user accordingly.

## Resquest example raw data : 
Creating a teacher on the `localhost:8000/account/register_teacher/` :
```json
{
    "username" : "green",
    "email" : "green@example.com",
    "password" : "Color.123",
    "password2" : "Color.123",
    "phone":"12345678",
    "subjects":["Mathématiques","Physique Chimie"],
    "introduction" : "The first teacher registered on the test database.",
    "diploma":null,
    "hourly_wage":"200",
    "disponibilities" :{"lundi":["8","9","16","17","18"],"mardi":["20","21"]}
}
```
Creating a student on the `localhost:8000/account/register_student/` :
```json
{
    "username" : "blue_student",
    "email" : "blue_student@example.com",
    "password" : "Color.123",
    "password2" : "Color.123",
    "phone":"92345678",
    "classe":"0",
    "speciality" : null
}
```
example de la reponse : 
```json
{
    "response": "Student registration successful!",
    "username": "blue_student",
    "email": "blue_student@example.com",
    "phone": 92345678,
    "is_student": true,
    "classe": "0",
    "speciality": null,
    "token": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDA2OTg0NCwiaWF0IjoxNjU5OTgzNDQ0LCJqdGkiOiIwNjcxMTIyOGI3Mjk0ODlhOTM3MWUyNzM1NjZmY2U5MCIsInVzZXJfaWQiOjEwfQ.Gju9-lru6UTpRtAT_h90EgRK8R2HMm_ULJri8Mc4WSI",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMDY5ODQ0LCJpYXQiOjE2NTk5ODM0NDQsImp0aSI6ImM3NTNlM2MzOTU3NDQ1NjRhZjI1YzBhZGVjODVmNDVhIiwidXNlcl9pZCI6MTB9.RrAcnR8pR0PDlyHqnTmQOFvMwAvdduVSL4xyfdSt3WM"
    }
}
```

Example : LessonOrderCreation :

```json
{
    "order":
    {
        "title" : "Cours math à domicile 4AS",
        "description":"Blah blah blah",
        "adresse" : "Nouakchott",
    },
    "subject" : [1],
    "hours" : 2,
    "unit_price" : 200,
    "students_count":2
}

```

## On deploiement setup:

creation of user platform,
`python manage.py createsuperuser --username "platform" --email "platform@gmail.com" --phone "+22299999999"`


or better launch the intial data setup file with :
`python manage.py loaddata fixtures.json`
creation of subjects :
Based on the subjects list


**Generate message files for a desired language**
`python manage.py makemessages -l fr`
`python manage.py makemessages -l ar`
 
**After adding translations to the .po files, compile the messages**
`python manage.py compilemessages`

## Common Errors :
if you encounter any errors while migrating you can delete the database 
from pgdmin and remove all the previous migration files
{
    "username" : "teacher_blue",
    "email" : "teacher_blue@example.com",
    "password" : "Color.123",
    "password2" : "Color.123",
    "phone":"10000001",
    "subjects":["Mathématiques","Physique Chimie"],
    "introduction" : "a blue teacher",
    "diploma":null,
    "hourly_wage":"200",
    "disponibilities" :{"Lundi":["8","9","16","17","18"],"Mardi":["20","21"]}
}