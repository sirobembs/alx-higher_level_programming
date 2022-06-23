#!/usr/bin/python3
"""Class that defines a square.
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
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints in stdout the square with the character #
        and if size is equal to 0, prints a new line.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
