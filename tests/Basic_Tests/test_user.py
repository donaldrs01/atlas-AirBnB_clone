#!/usr/bin/python3

import json
from models.user import User

user = User()

user.email = "test@hotmail.com"
user.password = "password123"
user.first_name = "Albert"
user.last_name = "Einstein"

user_dict = user.to_dict()

user_json = json.dumps(user_dict)

print(user_json)
