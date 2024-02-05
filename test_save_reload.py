#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

print(" -- Before Save --")
for obj_id, obj in storage.all().items():
    print(obj)

#  create new instance
test_model = BaseModel()
test_model.name = "Test model"
test_model.number = 15
print(test_model)

#  save the instance
test_model.save()

#  test print after save and reload
print(" -- After Save -- ")
for obj_id, obj in storage.all().items():
    print(obj)

# reload objects
storage.reload()

print(" -- After Reload -- ")
for obj_id, obj in storage.all().items():
    print(obj)
