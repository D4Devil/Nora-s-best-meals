#Set flask enviroment variable
$env:FLASK_APP = $PSSCriptRoot+"/src/norasBestMeals.py"

#Activate python's Virtual Eviroment (Needs Changes)
#source $(pipenv --venv)/bin/activate
. $PSSCriptRoot"/flask-venv/Scripts/activate.ps1"

#Start Flask app at localhost
flask run -h 0.0.0.0