#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  August 13, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Getting Started."""

import config

# DONE: Setting up 'black' formatter
# DONE: Creating Virtual Environment With 'virtualenv'
# DONE: Understanding Python modules
print(config.msg)  # hello from config.py

# DONE: Multiple assignment
filename = 'fonts.css'
file, ext = filename.split('.')

print(file + ' is a ' + '.' + ext + ' file')  # fonts is a .css file


# DONE: Double assignment
A = 32
x = y = z = A

print(x)  # 32
print(y)  # 32
print(z)  # 32

# DONE: The Unexpected 'UnboundLocalError' error
A = 1


def func():
    """Print a global variable value."""

    global A  # use global variable
    A += 1
    print(A)


func()  # 2


# DONE: The type() function and the __class__ method
items = 7, 's', 2.0, True, None, [1, 2], (1, 2), {1, 2}, {1: 2}, range(10)

print(items[0], type(items[0]))  # 7 <class 'int'>
print(items[1], type(items[1]))  # s <class 'str'>
print(items[2], type(items[2]))  # 2.0 <class 'float'>
print(items[3], type(items[3]))  # True <class 'bool'>
print(items[4], type(items[4]))  # None <class 'NoneType'>
print(items[5], type(items[5]))  # [1, 2] <class 'list'>
print(items[6], type(items[6]))  # (1, 2) <class 'tuple'>
print(items[7], type(items[7]))  # {1, 2} <class 'set'>
print(items[8], type(items[8]))  # {1: 2} <class 'dict'>
print(items[9], type(items[9]))  # range(0, 10) <class 'range'>
