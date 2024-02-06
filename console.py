#!/usr/bin/python3
"""Console module - entry point of command interpreter"""
import cmd
import json
import models
from models.base_model import BaseModel
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
