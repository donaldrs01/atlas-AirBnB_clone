#!/usr/bin/python3
"""Module for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel
    Public Class Attributes:
        place_id (str) : Place.id
        user_id (str) : User.id
        text (str) : text of the review"""
    place_id = ""
    user_id = ""
    text = ""
