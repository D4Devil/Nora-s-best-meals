#!/bin/bash

#Set flask enviroment variable
$env:FLASK_APP = $PSSCriptRoot+"/norasBestMeals.py"

#Activate python's Virtual Eviroment (Needs Changes)
#source $(pipenv --venv)/bin/activate

#Start Flask app at localhost
flask run -h 0.0.0.0