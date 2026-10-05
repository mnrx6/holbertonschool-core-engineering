#!/usr/bin/env python3
"""Append for reading a text file."""


def append_write(filename="", text=""):
    """Append and print a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
        return num
