#!/usr/bin/env python3
"""Define the BaseGeometry class."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raise an exception for area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
