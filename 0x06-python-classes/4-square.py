#!/usr/bin/python3

""" Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Init a new square.

        Args:
            size (int): The sizeof(the new square).
        """
        self.size = size

    @property
    def size(self):
        """Provide current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
