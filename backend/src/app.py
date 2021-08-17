from flask import Flask, request

app = Flask(__name__)


#Admin Routs
@app.route("/menu/", methods=['POST', 'GET'])
def menu():
    return "<p>Menu page<p>"


@app.route("/menu/main_courses/", methods=['POST','GET'])
def main_course():
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