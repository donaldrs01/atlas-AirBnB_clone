#!/usr/bin/python3
"""Console module - entry point of command interpreter"""
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand - basic command-line interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit the HBNBCommand interpreter
        Args:
            -"Quit" or "EOF" - to exit interpreter
        Returns:
            - True to exit"""
        return True

    do_EOF = do_quit  # alias for quit command

    def do_help(self, arg):
        """Provides help information for command interpreter
        Args:
            - command name (optional) to get help on command"""
        super().do_help(arg)  # calls do_help method of Cmd class

    def emptyline(self):
        """method in Cmd class that handles no input"""
        pass  # Do nothing on empty line

    def do_create(self, arg):
        """Command that creates new instance of BaseModel, saves it to the
            JSON, and prints the ID
        Args:
            - name of class instance to create"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Command that prints string representatn based on class name & ID"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        try:
            instance = storage.all()[f"{class_name}.{instance_id}"]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes instance based on class name & id, saves change to JSON file
        Args:
            - class name: name of class of instance
            - instance id: id of instance to delete"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]

        class_exists = False  # checks for class existence
        for key in storage.all().keys():  # iterates through storage dict
            if class_name in key:
                class_exists = True
                break  # breaks if class exists
        if not class_exists:
            print("** class doesn't exist **")
            return

        try:
            del storage.all()[f"{class_name}.{instance_id}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all str rprsntns of all instances based or not on class name
        Args:
            - class name: name of the class to filter instances"""
        if arg:
            try:  # filter instances based on class name
                instances = [
                    str(instance)
                    for instance in storage.all().values()
                    if instance.__class__.__name__ == arg
                ]
                print(instances)
            except NameError:
                print("** class doesn't exist **")
        else:
            instances = [str(instance) for instance in storage.all().values()]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on class name and ID by adding/updating
        attribute - changes then saved into JSON file
        Args:
            - class name: name of class of instance
            - instance id : ID of instance to update
            - attribute name : name of attribute to update
            - attribute value : updated value for given attribute"""
        #  args split into individual elements to allow for searching
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        class_exists = False
        for key in storage.all().keys():  # check if class exists
            if class_name in key:
                class_exists = True
                break
        if not class_exists:
            print("** class doesn't exist **")  # print error if no class
            return

        try:
            instance = storage.all()[class_name + "." + instance_id]
            # recreates dict key and retrieves instance to update
        except KeyError:  # raises error when key doesn't exist
            print("** no instance found **")
            return

        if (
            attribute_name != "id"
            and attribute_name != "created_at"
            and attribute_name != "updated_at"
        ):  # won't update ID or timestamp values
            if hasattr(instance, attribute_name):  # checks if name provided
                attribute_type = type(getattr(instance, attribute_name))
                if attribute_type == int:
                    #  int type conversion
                    attribute_value = int(attribute_value)
                elif attribute_type == float:
                    #  float type conversion
                    attribute_value = float(attribute_value)
            # updates attribute value
            setattr(instance, attribute_name, attribute_value)
            storage.save()  # saves updated instance into JSON file


if __name__ == "__main__":
    HBNBCommand().cmdloop()
