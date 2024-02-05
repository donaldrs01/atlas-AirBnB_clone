#!/usr/bin/python3

from base_model import BaseModel

testmodel = BaseModel(id = 34, description="This is a test.")
print(testmodel)
print(testmodel.to_dict())
