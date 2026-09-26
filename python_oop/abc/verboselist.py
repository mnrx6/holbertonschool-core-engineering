#!/usr/bin/env python3
"""This module defines a verbose list."""


class VerboseList(list):
    """Represent a list that prints modification messages."""

    def append(self, item):
        """Add an item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Add multiple items and print a message."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
