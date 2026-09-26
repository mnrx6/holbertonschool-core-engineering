#!/usr/bin/env python3
"""This module defines mixins and a dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
