from mongoengine import *
import os

connect("sanic_angular", host = os.environ['MONGODB_HOSTNAME'], port = 27017)

class Products(Document):
    name = StringField()
    description = StringField()
    precio = IntField()
    