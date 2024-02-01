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
            -"Quit" or "EQF" - to exit interpreter

        Returns:
            - True to exit
        """
        return True

    do_EQF = do_quit  # alias for quit command

if __name__ == "__main__":
    HBNBCommand().cmdloop()
