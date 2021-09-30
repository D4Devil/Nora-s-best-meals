import datetime
from enum import Enum
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import *
from flask_mongoengine import Document
from flask_user import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Roles(Document):
    name = StringField(max_length=255, required=True, primary_key=True)

    def get_id(self):
        return self.name


class Users(Document, UserMixin):
    username = StringField(max_length=64, primary_key=True)
    password = StringField(max_length=128, required=True)

    roles = ListField(ReferenceField(Roles))

    def get_id(self):
        return self.username


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    @staticmethod
    def validate_password(password_hash, password):
        return check_password_hash(password_hash, password)


class Meals(Document):
    name = StringField(max_length=255, required=True)
    description = StringField(max_length=600)


class Complements(Document):
    name = StringField(max_length=255, required=True)


class Desserts(Document):
    name = StringField(max_length=255, required=True)
    description = StringField(max_length=255)


class DaysOfTheWeek(Enum):
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'

    @classmethod
    def get_day_form_index(cls, index:int=0):
        """Return the day of the week of a given int
        following the pyhton's weekday. From 0 = monday
        to  4 = friday"""
        if index == 0:
            return cls.MONDAY
        elif index == 1:
            return cls.THURSDAY
        elif index == 2:
            return cls.WEDNESDAY
        elif index == 3:
            return cls.THURSDAY
        elif index == 4:
            return cls.FRIDAY
        else:
            raise IndexError("Out of range. Use 0:4 starting from monday")


class DayMenu(Document):
    day = EnumField(
            DaysOfTheWeek, 
            unique=True, 
            required=True, 
        )
    meals = ListField(ReferenceField(Meals))
    complements = ListField(ReferenceField(Complements))
    desserts = ListField(ReferenceField(Desserts))

    meta = {
        'max_documents': 5
    }


class Plates(EmbeddedDocument):
    meals = ListField(ReferenceField(Meals), required=True)
    complements = ListField(ReferenceField(Complements))
    desserts = ListField(ReferenceField(Desserts))
    coments = StringField(max_length=500)


class Orders(Document):
    name = ReferenceField(Users, required=True)
    plates = ListField(EmbeddedDocumentField(Plates))
    date = DateTimeField(default=datetime.datetime.utcnow(), required=True)