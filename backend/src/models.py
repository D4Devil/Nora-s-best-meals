from pyrebase.pyrebase import Database, PyreResponse
from .connector import FirebaseConnection as Fire
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
        Fire.get_database().child(cls.model_name) \
            .child(key).update(data)

    
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


class DayMenu(Model):
    model_name = 'day_menu'

    @classmethod
    def set(cls):
        pass


    @classmethod
    def update(cls, key, dishes:list, complements:list, desserts:list):
        return super().update(key, {'dishes':dishes, 'complements':complements, 'desserts':desserts})


class Order(Model):
    model_name = 'order'

    @classmethod
    def set(cls, dish, complement, dessert):
        return super().set({'dish':dish, 'complement':complement, 'dessert':dessert})


    @classmethod
    def update(cls, key, dish, complement, dessert):
        return super().update(key, {'dish':dish, 'complement':complement, 'dessert':dessert})



def print_model(data):
    count = 0
    for key, val in data.items():
        pprint(f"{count} -> {key} :: {val}")
        count += 1


def test_model():
    pprint(Dishes.get_data())

    if False:
        for count in range(0, 9):
            set_dish(f"Pozole {count}", "Yummi!")

    dishes = Dishes.get_data()
    print_model(dishes)
    
    pprint('Select a register to update')
    selection = int(input())

    key = list(dishes.keys())[selection]

    pprint(f"Updating: {key}:{Dishes.get(key)}")

    print("enter name: ")
    name = str(input())
    print("enter descript")
    desc = str(input())

    Dishes.update(key, name, desc)

    print_model(Dishes.get_data())


Order.get_data()