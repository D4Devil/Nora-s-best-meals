from pyrebase.pyrebase import Database, PyreResponse
from connector import FirebaseConnection as Fire
from pprint import pprint


class Model():

    @classmethod
    def get_data(cls):
        return Fire.get_database() \
                .child(cls.model_name).get().val()


    @classmethod
    def get(cls, key):
        return Fire.get_database().child(cls.model_name) \
                .child(key).get().val()


    @classmethod
    def set(cls, data):
        return Fire.get_database().child(cls.model_name) \
                .push(data)

    
    @classmethod
    def update(cls, key:str, data:dict):
        pprint(f"Updating {cls.model_name} register {key} to {data}")

    
    @classmethod
    def remove(cls, key:str):
        return Fire.get_database().child(cls.model_name).child(key).remove()


class Dishes(Model):

    model_name = 'dishes'

    @classmethod
    def set(cls, name, description):
        super().set({'name':name, 'description':description})


    @classmethod
    def update(cls, key, name, description):
        super().update(key, {'name':name, 'description':description})


class Complements(Model):

    model_name = 'complements'

    @classmethod
    def set(cls, name):
        return super().set({'name':name})


    @classmethod
    def update(cls, key:str, name):
        return cls.update(key, {'name':name})


class Desserts(Model):

    model_name = 'desserts'

    @classmethod
    def set(cls, name, description):
        return super().set({'name':name, 'description':description})

    
    @classmethod
    def update(cls, key:str, name, description):
        return super().update(key, {'name':name, 'description':description})

############################################################################

def get_dish(key:str) -> Database:
    return Fire.get_database().child('dishes').child(key).get().val()


def get_dishes():
    return Fire.get_database().child('dishes').get().val()


def set_dish(name, description = None):
    dishes_db = Fire.get_database().child('dishes')
    new_dish = {'name':name, 'description':description}
    return dishes_db.push(new_dish)


def update_dish(key, name, description):
    pass


def remove_dish(key):
    dishes_db = Fire.get_database().child('dishes')
    dishes_db.order_by_key().equal_to(key).remove()

############################################################


if __name__ == '__main__':
    pprint(Dishes.get_data())


    if False:
        for count in range(0, 9):
            set_dish(f"Pozole {count}", "Yummi!")

    dishes = Dishes.get_data()
    if dishes != None:
        counter = 0
        pprint('First Data:')
        for key, val in dishes.items():
            pprint(f"{counter} -> {key}:{val}")
            counter += 1
    
    pprint('Select a register to remove')
    selection = int(input())

    key = list(dishes.keys())[selection]

    pprint(f"Removing: {key}:{get_dish(key)}")

    dishes = Dishes.remove(key)
    pprint(Dishes.get_data())