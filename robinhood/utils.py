"""Utility functions."""
import re


def alpha_string(string):
    """Remove all special characters and numbers."""
    return re.sub("[^A-Za-z ]+", "", string)


def alphanumeric_string(string):
    """Remove all special characters and spaces."""
    return re.sub("[^A-Za-z0-9]+", "", string)
