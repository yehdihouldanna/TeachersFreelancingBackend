
# Local postgres configuration : 
username = postgres
password = postgres


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

## On deploiement setup:

launch the startup_project.py with shell


**Generate message files for a desired language**
`python manage.py makemessages -l fr`
`python manage.py makemessages -l ar`
 
**After adding translations to the .po files, compile the messages**
`python manage.py compilemessages`

## Common Errors :
if you encounter any errors while migrating you can delete the database 



### 
sudo systemctl restart gunicorn
sudo systemctl reload nginx
sudo systemctl status gunicorn