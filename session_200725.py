#!./venv/bin/python

# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  July 25, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education."""

import this


# DONE: The 'pip install -r <filename>' command
# DONE: Using .gitignore templates

# DONE: Docstrings (Document Strings)
def func(x, y):
    """Short line description.

    Extended description of function.

    :param x: description of x
    :type x: int

    :param y: description of y
    :type y: int

    :return: description of return value
    :rtype: int
    """
    return x * y


print(func.__doc__)
help(func)

# DONE: The Zen of Python
