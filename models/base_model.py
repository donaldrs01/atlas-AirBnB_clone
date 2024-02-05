#!/usr/bin/python3

import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class declaration
    Defines shared attributes/methods for sub classes"""
    def __init__(self, *args, **kwargs):
        """Constructor for new BaseModel instance
        Args:
            args: Variable number of non-keyword args
            kwargs: Variable number of keyword args collected in dict
        Attributes:
            id (str) : unique identifier number (assigned with uuid)
            created_at (datetime) : creation timestamp
            updated_at (datetime) : updated whenever changes made to obj"""
        if kwargs:
            for key, value in kwargs.items():  # iterates over key-value pairs
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':  # avoid overriding class attribute
                    setattr(self, key, value)
        else:  # no provided values for id, created_at, updated_at
            self.id = str(uuid.uuid4())  # generate UUID
            self.created_at = self.updated_at = datetime.now()  # initialize timestamps
            models.storage.new(self)  # adds instance to FileStorage dict
    
    def __str__(self):
        """Provides str representation of BaseModel instance
        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__  # retrieve class name
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates attribute 'updated_at' with current datetime"""
        from . import storage  # import storage here to avoid circular import
        self.updated_at = datetime.now()
        storage.save()  #  add FileStorage saving mechanisms to instance
    
    def to_dict(self):
        """Returns dict representation of BaseModel instance
        Returns:
            dict : dictionary printout with key-value pairs of instance"""
        base_copy = self.__dict__.copy()  # copy dictionary and key/values
        base_copy['created_at'] = self.created_at.isoformat()
        base_copy['updated_at'] = self.updated_at.isoformat()
        base_copy['__class__'] = self.__class__.__name__
        return base_copy  # return modified dictionary
