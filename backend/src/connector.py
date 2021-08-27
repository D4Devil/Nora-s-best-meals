from pprint import pprint
import pyrebase
from pyrebase.pyrebase import Database, Firebase


class FirebaseConnection():
    firebase_config = {
            "apiKey": "AIzaSyCBWuMRBxfOtvtHLUE6PLM9LB1Qr4w-5hw",
            "authDomain": "birkman-13bd4.firebaseapp.com",
            "projectId": "birkman-13bd4",
            "storageBucket": "birkman-13bd4.appspot.com",
            "messagingSenderId": "975918929531",
            "appId": "1:975918929531:web:7c06ea22177e40e0a2f4de",
            "databaseURL":"https://birkman-13bd4-default-rtdb.firebaseio.com/"
        }

    @staticmethod
    def get_app() -> Firebase:
        if FirebaseConnection._app == None:
            pprint("Connecting to firebase")
            FirebaseConnection._app = pyrebase.initialize_app(FirebaseConnection.firebase_config)
        return FirebaseConnection._app

    @staticmethod
    def get_database() -> Database:
        return  FirebaseConnection.get_app().database()


    @staticmethod
    def populate():
        FirebaseConnection.get_database.push()

    _app: Firebase = None

    