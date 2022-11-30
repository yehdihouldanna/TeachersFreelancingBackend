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

# PRODUCTION SETUP: 

## To reset the database if needed : 

`sudo -u postgres psql`

```sql
DROP DATABASE IF EXISTS teacher_freelance;

CREATE DATABASE teacher_freelance;
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE teacher_freelance TO postgres;
\q
```

## Initial project setup : 

*Activate the virtual environemeent :* 
```sh
source teacher_freelance_env/bin/activate
cd TeachersFreelancingBackend
```

*Make migrations*
```sh
python manage.py makemigrations
python manage.py migrate
```

if you encounter any problems in migrations reset the database.



*Collectstatic files :* 
`python manage.py collectstatic`

*Initial database entries :*

launch the startup_project.py with shell
```sh
    $ python manage.py shell
    >>> exec(open("setup_project.py").read())
```


**Generate message files for a desired language**
`python manage.py makemessages -l fr`
`python manage.py makemessages -l ar`
 
**After adding translations to the .po files, compile the messages**
`python manage.py compilemessages`

## To start the project on server :
```sh

sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl status gunicorn

sudo systemctl restart nginx
```

## Common Errors :
if you encounter any errors while migrating you can delete the database 


## Nginx config : 
`/etc/nginx/sites-available/default`

```yml
##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# https://www.nginx.com/resources/wiki/start/
# https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
# https://wiki.debian.org/Nginx/DirectoryStructure
#
# In most cases, administrators will remove this file from sites-enabled/ and
# leave it as reference inside of sites-available where it will continue to be
# updated by the nginx packaging team.
#
# This file will automatically load configuration files provided by other
# applications, such as Drupal or Wordpress. These applications will be made
# available underneath a path with that package name, such as /drupal8.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

# Default server configuration
#
server {
	listen 80 ;
	listen [::]:80 ;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name 161.35.76.153;

	location = /favicon.ico { access_log off; log_not_found off; }
	location /static/ {
        alias /home/user/TeachersFreelancingBackend/staticfiles/;
    }
	location /media/ {
        alias /home/user/TeachersFreelancingBackend/media/;
    }
	location /document_files/ {
        alias /home/user/TeachersFreelancingBackend/document_files/;
    }
	location /teachers_diplomes/ {
        alias /home/user/TeachersFreelancingBackend/teachers_diplomes/;
    }
	
	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		include proxy_params;
        proxy_pass http://unix:/home/user/TeachersFreelancingBackend/teacher_freelance.sock;
		# try_files $uri $uri/ =404;
	}

	# pass PHP scripts to FastCGI server
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
	#	fastcgi_pass unix:/run/php/php7.4-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
```