#!/usr/bin/python3

from .engine.file_storage import FileStorage

storage = FileStorage()  # instance created for reload
storage.reload()  # deserializes from JSON into dict
