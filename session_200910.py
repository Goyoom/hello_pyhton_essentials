#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  September 10, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Variable, Booleans, and Operators."""

from decimal import Decimal
from fractions import Fraction

# Done: Variables Are Names
x = [1, 2]
y = x

y.append(3)  # [1, 2, 3]

print(x, id(x))  # [1, 2, 3] 4566590208
print(y, id(y))  # [1, 2, 3] 4566590208

a = 5
b = a

b += 1

print(a, id(a))  # 5 4360444592
print(b, id(b))  # 1 4360444464

# DONE: Python's falsy values
print('--------Python\'s falsy values--------')

falsy = None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), list(), set(), tuple(), dict(), '', b'', range(0)

print(bool(falsy[0]))  # False
print(bool(falsy[1]))  # False
print(bool(falsy[2]))  # False
print(bool(falsy[3]))  # False
print(bool(falsy[4]))  # False
print(bool(falsy[5]))  # False
print(bool(falsy[6]))  # False
print(bool(falsy[7]))  # False
print(bool(falsy[8]))  # False
print(bool(falsy[9]))  # False
print(bool(falsy[10]))  # False
print(bool(falsy[11]))  # False
print(bool(falsy[12]))  # False
print(bool(falsy[13]))  # False

age = 16
is_adult = age >= 18

print(is_adult)  # False

# DONE: Logical Operators, and, or, not
print('--------Logical Operators, and, or, not--------')

print(1 < 5 and 1 < 10)  # True, True if both sides true.
print(1 > 5 or 1 < 10)  # True, True if one side is true.
print(not True)  # False, true if false, false if true

# DONE: Logical Operators Precedence (not, and, then or)
print('--------Logical Operators Precedence--------')

# Accept the person who is designer and developer, or a learner.
is_designer = True
is_developer = False
is_learner = True

is_accepted = is_designer and is_developer or is_learner

print(is_accepted)  # True, identical to...is_accepted = (is_designer and is_developer) or is_learner
