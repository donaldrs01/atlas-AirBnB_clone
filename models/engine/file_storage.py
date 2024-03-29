#!/usr/bin/python3
"""File storage module doc"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
        files into instances
    Private class attributes:
        __file_path (str) : path to the JSON file (ex: file.json)
        __objects (dict) : empty but will store all objects by
        <class name>.id
            Ex: BaseModel obj with id=12121212 -> BaseModel.12121212
    Public instance methods:
        all(self): returns dictionary containing all __objects
        new(self, obj): adds new object to __objects dictionary
            Uses the class name and object's 'id' as the key
        save(self): serializes the __objects dictionary into JSON file
        reload(self): deserializes (reloads) JSON file back into
        __objects dict"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all objects
            stored in the __objects attribute
        Returns:
            dict: keys are in format <class name>.<id> and values
            are corresponding objects"""
        return FileStorage.__objects  # class attribute
        #  shared dictionary across all instances of class

    def new(self, obj):
        """Adds new object to __objects dictionary
            Uses the class name and object's ID as the key
        Args:
            obj: Object to be added  to __objects dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"  # cnstrcts key w/ obj info
        FileStorage.__objects[key] = obj  # add obj to cls dict w/ correct key

    def save(self):
        """Serializes dict pairs of objects and saves to .json files"""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():  # iterate thru pairs
            serialized_objs[key] = obj.to_dict()  # serialize and store

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)  # saves as JSON file

    def reload(self):
        """Reloads stored JSON representations back into __obj dictionary"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objs = json.load(file)  # load JSON files into dict

                # handle different subclasses
                class_mapping = {
                        "BaseModel": BaseModel,
                        "Place": Place,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Review": Review
                }
            for key, value in loaded_objs.items():
                class_name = value.get("__class__")
                if class_name in class_mapping:
                    cls = class_mapping[class_name]
                    obj = cls(**value)  # create instance of correct class
                    FileStorage.__objects[key] = obj  # store w/ original ID

        except FileNotFoundError:
            pass  # Do nothing if file doesn't exist
