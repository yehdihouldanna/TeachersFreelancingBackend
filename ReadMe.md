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



## Resquest example raw data : 
Creating a teacher on the `localhost:8000/account/register_teacher/` :
```json
{
    "username" : "green",
    "email" : "green@example.com",
    "password" : "Color.123",
    "password2" : "Color.123",
    "phone":"12345678",
    "subjects":{"Math":[],"Physics":[]},
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

## Common Errors :

if you encounter any errors while migrating you can delete the database from pgdmin and remove all the previous migration files