from flask import Flask, json, request
from flask.helpers import url_for
from flask_login import current_user, login_manager, login_user
from flask_login.utils import logout_user
from flask_user.decorators import login_required, roles_required
from mongoengine.errors import OperationError
from werkzeug.utils import redirect
from .models import *
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_user import UserManager
from .models import *
from .flask_config import Config
from pprint import pprint


def start_app(test_config = None, set_db = False):
    app = Flask(__name__)
    app.config.from_object(Config)

    app_cors = CORS(app)

    db = MongoEngine(app)

    user_manager__ = UserManager(app, db, Users)
    login_manager__ = login_manager.LoginManager()
    login_manager__.init_app(app)

    if set_db:
        set_database()

    return app, app_cors, user_manager__, login_manager__


def set_database():
    try:
        Users.drop_collection()
        
    except OperationError:
        print("The collection was empty or doesn't exist")
    
    admin = Roles(name='admin').save()
    client = Roles(name='client').save()

    admin_user = Users(username='damian')
    admin_user.roles = [admin]
    admin_user.set_password('d4')
    admin_user.save()

    non_admin = Users(username='not damian')
    non_admin.roles = [client]
    non_admin.set_password('d4')
    non_admin.save()

    pozole = Meals(name='Pozolito', description='delicioso').save()
    Meals(name='Tamales', description='calientitos').save()

    arroz = Complements(name='Arroz').save()
    Complements(name='Frijoles').save()

    helado = Desserts(name='Helado', description='de shokolate').save()
    Desserts(name='Marquesita', description='Con nutella o doble queso').save()

    day_menu = DayMenu(day=DaysOfTheWeek.MONDAY)
    day_menu.meals = [pozole]
    day_menu.complements = [arroz]
    day_menu.desserts = [helado]
    day_menu.save()

    plate_01 = Plates(coments="no salsa plz")
    plate_01.meals = [pozole]
    plate_01.complements = [arroz]
    plate_01.desserts = [helado]

    order_01 = Orders(name=non_admin)
    order_01.plates = [plate_01]
    order_01.save()


app, app_cors, user_manager__, login_manager__ = start_app()


@login_manager__.user_loader
def load_user(id):
    return Users.objects(username=id).first()


### Routing paths ###
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = Users.objects(username=data['username']).first()
    if current_user.is_authenticated and user == current_user:
        #TODO:[Change] maybe logout and redirect to the login page? idk sound akward
        return "Already auth"

    if user is None or not user.validate_password(user.password, data['password']):
        #TODO:[Change] Return api response for none matching users or password
        return "username or password don't match"

    if login_user(user):
        #Succesful login
        #TODO:[Change] provisional return, should use next:(url) as a rquest paramaeter
        return "a new url to redirect"

    return "Exception: user cannot be loaded"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/", methods=['GET'])
def index():
    """Returns the today's menu calculated with the server
    configured date.
    
    methods: 'GET'
    routes: '/'
    """
    #TODO:[Change] This sould just rediret to '/day_menu/today'
    try:
        todays_weekday = DaysOfTheWeek.get_day_form_index( \
                datetime.datetime.today().weekday())
        return DayMenu.objects(day=todays_weekday).to_json()
    except:
        #TODO:[Define] What should I display when today is weekend
        return "Sorry, today we're resting"


@app.route("/users", methods=['GET', 'POST', 'DELETE'])
@roles_required('admin')
def user_crud():
    data = request.json

    if request.method == 'GET':
        return Users.objects().to_json()
    
    elif request.method == 'POST':
        new_user = Users(username=data['username'])
        new_user.set_password(data['password'])

        print(Roles.objects(name__in=data['roles']))
        new_user.roles = Roles.objects(name__in=data['roles'])

        new_user.save()
        return 'TODO: Send ok'

    elif request.method == 'DELETE':
        to_delete:Users = Users.objects(
                username=request.json['username']
            ).first()

        if to_delete is not None:
            to_delete.delete()
            return 'TODO: Return Deleted'
            
        else:
            return 'TODO: User not found'


@app.route("/meals", methods=['GET'])
def get_meals():
    """Return the complete list of meals objects on json format.

    methods: 'GET'
    routes: '/meals'

    Content-Type: application/json

    If failed returns an empty list
    """
    return Meals.objects.to_json()


@app.route("/meal/<string:id>", methods=['GET', 'PUT', 'POST', 'DELETE'])
@roles_required('admin')
def meals_crud(id):
    """[GET]: Returns the specific meal object for the given id.
    [PUT]: Updates the object with the given id.
    [POST]: Use 'new' to create a new object with an autogenerated id.
    [DELETE]: Deletes the object with the given id.
    
    methods: 'GET', 'POST', 'DELETE'
    routes: '/meals/<str:id>', '/meals/new'
    """
    if request.method == 'GET':
        return Meals.objects(id=id).first().to_json()

    elif request.method == 'DELETE':
        obj = Meals.objects(id=id).first()
        obj.delete()
        
        #TODO:[define]
        return f'Deleted {id}'

    data = request.json
    name = data['name']
    descript = data['description']

    if request.method == 'POST':
        ##Update
        obj = Meals(name=name, description=descript)
        obj.save()
        return 'Ok'

    elif request.method == 'PUT':
        obj:Meals = Meals.objects(id=id).first()
        obj.name = name
        obj.description = descript
        obj.save()
        return 'Ok'


@app.route("/complements", methods=['GET'])
def get_complements():
    """Return the complete list of complements objects on json format.

    methods: 'GET'
    routes: '/complements'

    Content-Type: application/json

    If failed returns an empty list
    """
    return Complements.objects.to_json()


@app.route("/complements/<string:id>", methods=['GET', 'PUT', 'POST', 'DELETE'])
@roles_required('admin')
def complements_crud(id):
    """Returns the specific complements object for the given id.
    
    methods: 'GET', 'POST', 'DELETE'
    routes: '/complements/<str:id>'
    """
    if request.method == 'GET':
        return Complements.objects(id=id).first().to_json()

    elif request.method == 'DELETE':
        obj = Complements.objects(id=id).first()
        obj.delete()
        
        #TODO:[define]
        return f'Deleted {id}'

    data = request.json
    name = data['name']

    if request.method == 'POST':
        obj = Complements(name=name)
        obj.save()
        return f'Saved: {obj.to_json()}'
        
    elif request.method == 'PUT':
        ##Update
        obj:Complements = Complements.objects(id=id).first()
        obj.name = name
        obj.save()
        return f'Updated: {obj.to_json()}'



@app.route("/desserts", methods=['GET'])
def get_desserts():
    return Desserts.objects.to_json()


@app.route("/desserts/<string:id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
@roles_required('admin')
def desserts_crud(id):
    if request.method == 'GET':
        return Desserts.objects(id=id).to_json()

    elif request.method == 'DELETE':
        obj = Desserts.objects(id=id).first()
        obj.delete()
        return f'Deleted {id}'

    data = request.json
    name = data['name']
    descript = data['description']

    if request.method == 'POST':
        obj:Desserts = Desserts(name=name, description=descript)
        obj.save()
        return f'Saved: {obj.id}'

    elif request.method == 'PUT':
        obj:Desserts = Desserts.objects(id=id).first()
        obj.name = name
        obj.description = descript

        obj.save()
        return obj.to_json()


@app.route("/day_menu/<string:day>", methods=['GET'])
def get_day_menu(day):
    """TODO"""

    # Get the day menu object in order to update it or return 
    if day == 'today':
        todays_weekday = DaysOfTheWeek.get_day_form_index( \
                    datetime.datetime.today().weekday()).value
        day_menu:DayMenu = DayMenu.objects(day=todays_weekday).first()

    else:
        todays_weekday = day
        day_menu:DayMenu = DayMenu.objects(day=todays_weekday).first()

    if request.method == 'GET':
        json_menu = {'day':todays_weekday,
                'menu':{
                    'meals': day_menu.meals,
                    'complements': day_menu.complements,
                    'desserts':day_menu.desserts
                }}
            
        return json.dumps(json_menu)


@app.route("/day_menu/<string:day>", methods=['PUT'])
@roles_required('admin')
def update_day_menu(day):

    # Get the day menu object in order to update it or return 
    if day == 'today':
        todays_weekday = DaysOfTheWeek.get_day_form_index( \
                    datetime.datetime.today().weekday()).value
        day_menu:DayMenu = DayMenu.objects(day=todays_weekday).first()

    else:
        todays_weekday = day
        day_menu:DayMenu = DayMenu.objects(day=todays_weekday).first()

    data = request.json
    jmeals = data['meals']
    jcomplements = data['complements']
    jdesserts = data['desserts']

    day_menu.meals = Meals.objects(
            id__in=[_meal['_id']['$oid'] for _meal in jmeals]
        )
    day_menu.complements == Complements.objects(
            id__in=[_comp['_id']['$oid'] for _comp in jcomplements]
        )
    day_menu.desserts == Desserts.objects(
        id_in=[_dess['_id']['$oid'] for _dess in jdesserts]
    )

    day_menu.save()


@app.route("/orders", methods=['GET', 'POST'])
@login_required
def orders_crud():
    user:Users = current_user._get_current_object()

    if request.method == 'GET':
        if user.has_roles('admin'):
            return Orders.objects.to_json()

        else:
            return Orders.objects(name=user.id).to_json()
        
    elif request.method == 'POST':
        data = request.json()

        plates_list = []
        for plate in data['plates']:
            plate_obj = Plates(coments=plate['comments'])
            plate_obj.meals = Meals.objects(
                    id__in=[_meals['_id']['$oid'] for _meals in plate['meals']]
                )
            plate_obj.complements = Complements.objects(
                    id__in=[_comp['_id']['$oid'] for _comp in plate['complements']]
                )
            plate_obj.desserts = Desserts.objects(
                    id__in=[_dess['_id']['$oid'] for _dess in plate['desserts']]
            )
            plates_list.append 

        new_order = Orders(name=user.username)
        new_order.plates = plates_list
        new_order.save()

        return f'Order saved {new_order.to_json()}'