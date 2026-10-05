#!/usr/bin/env python3
"""Module for writeing a text file."""


def write_file(filename="", text=""):
    """Write and print a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
        return num
