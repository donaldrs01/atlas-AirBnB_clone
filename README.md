# atlas-AirBnB_clone
Welcome to the AirBnB clone project.

## description of the project
This project is a clone of the airbnb command interpreter, so we can manipulate data without a visual interface.

## description of the command interpreter
The command interpreter is a program written in Python that allows users to interact with an AirBnB clone application through a CLI. It provides a set of commands that users can use to perform various actions, such as creating, showing, updating, and deleting instances of different classes in the application.

## Starting the command interpreter
You can start the command interpreter with the Python interpreter after downloading the project and entering `python3 console.py` into your terminal at the root of the project directory.

## Using the command interpreter
You use the command interpreter by entering your command (hint: start with `help`), then by following the syntax and error descriptions. 

## Usage examples
```
(hbnb)create BaseModel
11a1aa1a-2bb2-3c3c-d44d-5e55ee5ee555
(hbnb)...
```
In this example, an instance of the BaseModel class has been created, and the ID of the instance was returned.


```
(hbnb)update BaseModel 11a1aa1a-2bb2-3c3c-d44d-5e55ee5ee555 satisfaction 3
[BaseModel] (11a1aa1a-2bb2-3c3c-d44d-5e55ee5ee555) {'id': '11a1aa1a-2bb2-3c3c-d44d-5e55ee5ee555', 'created_at': datetime.datetime(2024, 1, 2, 3, 4, 5, 123456), 'updated_at': datetime.datetime(2024, 6, 7, 8, 9, 10, 789100), 'satisfaction': '3'}
(hbnb)...
```
In this example, the BaseModel class instance created previously has been updated to include a new attribute called satisfaction with a value of 3. The command returned the ID, time created, time updated, and the new attribute.
