#!/usr/bin/python3

"""Class Square."""


class Square:
    """Square."""

    def __init__(self, size=0):
        """Init a new Square.

        Args:
            size (int): The sizeof(the new square).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
