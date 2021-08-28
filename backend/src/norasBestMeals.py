from flask import Flask, request
from .models import Dishes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#Admin Routs
@app.route("/", methods=['POST', 'GET'])
def menu():
    return Dishes.get_data()


@app.route("/admin/", methods=['POST','GET'])
def main_admin():
    return "<p>Main Courses<p>"


@app.route("/menu/main_courses/<int:id>")
def edit_main_course(id):
    pass


@app.route("/menu/complements/")
def complements():
    pass


@app.route("/menu/complements/<int:id>")
def edit_complement(id):
    pass


@app.route("/menu/desserts/")
def desserts():
    pass


@app.route("/menu/desserts/<int:id>")
def edit_dessert(id):
    pass