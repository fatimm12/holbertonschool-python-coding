#!/usr/bin/python3
"""
This module defines a Square class used to represent a geometric square.
It will serve as a foundation for further development such as area calculation.
"""

class Square:
    """
    A class to represent a geometric square with size information.

    Attributes:
        __size (int): The size (length of side) of the square, stored privately.
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the square object.

        Args:
            size (int): The size of the square side, no validation is done here.
        """
        self.__size = size

