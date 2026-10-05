#!/usr/bin/env python3
"""Module for reading a text file."""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
