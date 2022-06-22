#!/usr/bin/python3
"""Class that defines a square by it size,
and also the sqare area.
"""
class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Method that returns the current square area.
        """
        return (self.__size ** 2)
