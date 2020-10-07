#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All rights are reserved.
#  September 19, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Identity and Membership Operators, type Annotation, functional programming, and Lambda Function"""


# DONE: Identity Operators, 'is' and 'is not'
attr = True

# bad practice
if attr == True:
    print('attr is True')

# better practice
if attr:
    print('attr is True')


# best practice
if attr is True:
    print('attr is True')

else:
    print('attr is not True')

# DONE: Membership Operators, 'in' and 'not in'
msg = 'hello'
nums = ['1', '2', '3']  # any sequence (string, list, or tuple)

print('h' in msg)  # True
print('1' in nums)  # True
print('4' in nums)  # False


# DONE: Type Annotations
def add(x: int, y: int) -> list:
    return [
        x + y,
    ]


print(add(1, 2))  # [3]


# DONE: Functional Programming
def fib(m):
    """Fibonacci series

    The sum of two elements defines the next."""
    output = list()  # []
    a, b = 0, 1
    while a < m:
        output.append(a)
        a, b = b, a + b

    return output


print(fib(100))

# DONE: Lambda Functions
add = lambda x, y: x + y  # noqa

# identical to lambda:
# def add(x, y):
#     return x + y

nums = [13, 13, 15, 2, 8, 48, 10]

print(list(filter(lambda x: x != 2, nums)))  # [13, 13, 15, 8, 48, 10]
