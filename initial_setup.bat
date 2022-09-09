echo "You are running the default setting up script"
echo "Please place yourself in the folder of the repository before executing the rest of this script"
echo "Do you want to continue  y/n : "
read input
if [[ $input =="Y"   ||  $input == "y"]]; then
echo "you answered yes"
else echo "you answered no"

@REM # TODO Create a postgres data base name teacher_freelance

@REM echo "Creating the python environment in the repository"
@REM python -m venv teacher_freelance_env    
@REM cd ..
@REM teacher_freelance_env/Scripts/activate
@REM echo "Creating a superuser"
@REM cd teacher_freelance
@REM python manage.py createsuperuser --username "platform" --email "platform@gmail.com" --phone "+22299999999" 
 
@REM python manage.py runserver