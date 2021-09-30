#Set flask enviroment variable
$env:FLASK_ENV = "development"
$env:FLASK_APP = $PSSCriptRoot+"/flaskr/norasBestMeals.py"

#Activate python's Virtual Eviroment (Needs Changes)
#source $(pipenv --venv)/bin/activate
. $PSSCriptRoot"/flask-venv/Scripts/activate.ps1"

#Start mongo's local db
#& "C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe"

#Start Flask app at localhost
flask run -h 0.0.0.0