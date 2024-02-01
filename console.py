#!/usr/bin/python3
"""
Console module - entry point of command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - basic command-line interpreter
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit the HBNBCommand interpreter

        Args:
            -"Quit" or "EOF" - to exit interpreter

        Returns:
            - True to exit
        """
        return True

    do_EOF = do_quit  # alias for quit command

    def do_help(self, arg):
        """
        Provides help information for command interpreter

        Args:
            - command name (optional) to get help on command
        """
        super().do_help(arg)  # calls do_help method of Cmd class

    def emptyline(self):
        """
        method in Cmd class that handles no input
        """
        pass  # Do nothing on empty line

if __name__ == "__main__":
    HBNBCommand().cmdloop()
