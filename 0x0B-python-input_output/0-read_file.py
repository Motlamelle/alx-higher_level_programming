#!/usr/bin/python3
"""
This function reads a text file and prints to STDOUT
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
