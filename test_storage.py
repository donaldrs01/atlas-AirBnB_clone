#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
user1 = User()
user2 = User()
place1 = Place()
state1 = State()
review1 = Review()

storage = FileStorage()
storage.new(user1)
storage.new(user2)
storage.new(place1)
storage.new(state1)

storage.save()

storage.reload()

all_objects = storage.all()

for obj_key, obj in all_objects.items():
    print(obj_key, obj)
    print()
