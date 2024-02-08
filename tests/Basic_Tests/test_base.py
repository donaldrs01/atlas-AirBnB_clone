#!/usr/bin/python3
from models.base_model import BaseModel

test_model = BaseModel()
test_model.name = "Test model"
test_model.number = 40

print("Original BaseModel Instance:")
print(test_model)

test_model_json = test_model.to_dict()

print("JSON of test:")
for key in test_model_json.keys():
    print(f"{key}: ({type(test_model_json[key])}) - {test_model_json[key]}")
