from random import sample
from pymongo import MongoClient
from pprint import pprint
import certifi

DATABASE_NAME = "birkman-test02"
CONNECTION_STRING = "mongodb+srv://dm:d4@birkmancluster0.68blf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
SAMPLE_DATA = {"sample_data": 
                {
                    "list": [1,2,3]
                }
            }


def get_database_connection():
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    return client['test-database']


conn = get_database_connection()
db = conn[DATABASE_NAME]
collection = db['main-course']

pprint(collection)
id = collection.insert_one({"sample_data":"sample string"}).inserted_id()