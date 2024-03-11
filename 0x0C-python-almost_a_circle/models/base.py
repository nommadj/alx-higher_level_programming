#!/usr/bin/python3
"""This module is the definition of a class"""


class Base:
    """This is a definition of a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a constructor method
            args:
                id= id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
