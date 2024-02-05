#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel

    Public Class Attributes:
        email (str) : User's email address
        password (str) : User's password
        first_name (str) : User's first name
        last_name (str) : User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()  # calls BaseModel constructor
        #  has User attributes as well as BaseModel attributes
