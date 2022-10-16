echo "You are running the default setting up script"
echo "Please place yourself in the folder of the repository before executing the rest of this script"
echo "Do you want to continue  y/n : "
@REM read input
@REM if [[ $input =="Y"   ||  $input == "y"]]; then
@REM echo "you answered yes running the setup script"
@REM TODO Create a postgres data base name teacher_freelance

@REM echo "Creating the python environment in the repository"
@REM python -m venv teacher_freelance_env    
cd ..
@REM teacher_freelance_env/Scripts/activate
@REM cd teacher_freelance
echo "installing related modules"
@REM pip install requirements.txt

echo "Collecting the static files"
CALL C:\Users\yehdi\Documents\Projects\TeacherFreelance\teacher_freelance_env\Scripts\activate.bat && python "C:\Users\yehdi\Documents\Projects\TeacherFreelance\teacher_freelance\manage.py" collectstatic --no-input

echo "Setting up initial of basic entities"
C:\Users\yehdi\Documents\Projects\TeacherFreelance\teacher_freelance_env\Scripts\activate.bat && python "C:\Users\yehdi\Documents\Projects\TeacherFreelance\teacher_freelance\manage.py" shell -c "exec(open('setup_project.py').read()"

@REM echo "Launching the sever"
@REM python manage.py runserver

