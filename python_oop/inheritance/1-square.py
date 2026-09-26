#!/usr/bin/env python3
"""Define the Rectangle class."""


Rectangle = __import__("2-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square area."""
        return self.__size * self.__size
