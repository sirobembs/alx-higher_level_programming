#!/usr/bin/python3
import math
"""A class that calculate the circumfrence and perimeter
when given a radius.
"""


class MagicClass:
    """Class that stores the propertiesof a circumference
    """
    def __init__(self, radius=0):
        """Method that initialize the radius of the circumference
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Method that calculates the area of the circumfernce
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Method that calculates the perimeter of a circumference
         """
        return (2 * math.pi * self.__radius)
