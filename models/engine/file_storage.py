#!/usr/bin/python3

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file
    s into instances

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
        __objects dict
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method that returns a dictionary containing all objects
        stored in the __objects attribute

        Returns:
            dict: keys are in format <class name>.<id> and values
            are corresponding objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds new object to __objects dictionary
        Uses the class name and object's ID as the key

        Args:
            obj: Object to be added  to __objects dictionary
        """
        key = f"({obj.__class__.__name__}.{obj.id}"  # constructs key with obj info
        self.__objects[key] = obj  #  add obj to dictionary with correct key
