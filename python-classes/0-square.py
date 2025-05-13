#!/usr/bin/python3
"""
This module defines a Square class used to represent a geometric square.

The Square class stores the size of the square privately
and serves as a base for further functionality like area computation.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored privately.
    """

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of one side of the square.
        """
        self.__size = size

