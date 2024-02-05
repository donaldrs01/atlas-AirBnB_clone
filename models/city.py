#!/usr/bin/python3
"""
Module for City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel

    Public Class Attributes:
        state_id (str) : state.id to tie it to state
        name (str) : name of city
    """
    state_id = ""
    name = ""
