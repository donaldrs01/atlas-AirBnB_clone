#!/usr/bin/python3

from base_model import BaseModel

testmodel = BaseModel(name="Test", description="This is a test.")
print(testmodel)
print(testmodel.to_dict())
