#!/usr/bin/bash
"""This is a square class that inherits Rectangle"""

from .rectangle import Rectangle

class Square(Rectangle):
    """This is a class initialization"""
    def __init__(self, size, x=0, y=0, id=None):
        """This is a constructor"""
        super().__init__(size, size, x, y, id)

    
    def __str__(self):
        """Prints string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width
                if hasattr(self, 'width') else self.height)

    @property
    def size(self):
        """This is getter"""
        return self.width

    @size.setter
    def size(self, value):
        """This is a setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value 
