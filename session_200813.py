#!./venv/bin/python

# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  July 25, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education."""

import config

# DONE: Setting up 'black' formatter
# DONE: Understanding Python modules
print(config.msg)

# DONE: Multiple assignment
filename = 'fonts.css'
file, ext = filename.split('.')

print(file + ' is a ' + ext + ' file')

# DONE: Double assignment
a = 32
x = y = z = a

print(x)  # 32
print(y)  # 32
print(z)  # 32

# DONE: The Unexpected 'UnboundLocalError' error
a = 1


def func():
    global a  # use global variable
    a += 1
    print(a)


func()  # 2


# DONE: The type() function and the .__class__ method
items = 7, 's', 2.0, True, None, [1, 2], (1, 2), {1, 2}, {1: 2}, range(10)

print(items[0], type(items[0]))
print(items[1], type(items[1]))
print(items[2], type(items[2]))
print(items[3], type(items[3]))
print(items[4], type(items[4]))
print(items[5], type(items[5]))
print(items[6], type(items[6]))
print(items[7], type(items[7]))
print(items[8], type(items[8]))
print(items[9], type(items[9]))
