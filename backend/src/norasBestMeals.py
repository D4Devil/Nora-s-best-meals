from flask import Flask, request
from .models import *
from flask_cors import CORS


app = Flask(__name__)
app_cors = CORS(app)


#Admin Routs
@app.route("/")
def todays_menu():
    return DayMenu.get_data()


@app.route("/dishes/")
def dishes():
    return Dishes.get_data()


@app.route("/complements/")
def complements():
    return Complements.get_data()


@app.route("/desserts/")
def desserts():
    return Desserts.get_data()


@app.route("/orders/")
def orders():
    return Order.get_data()