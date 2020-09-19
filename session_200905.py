#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  September 5, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Numbers."""
from decimal import Decimal
from fractions import Fraction

# DONE: Python has only two types of numbers, integer and float
a, b = 7, 2.0

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

# DONE: Adding leading zero
c = -2

print(f'{a:02}')  # 07
print(f'{c:02}')  # -2

# DONE: Floor division operator
d = 12 / 3
e = 12 // 3

print(d)  # 4.0
print(e)  # 4
print(type(e))  # <class 'int'>

# DONE: Inaccurate floating-point values
# Warning: Using floats to represent currency, or anything that requires accuracy should be always avoided.

f = 1.2
"""The number 1.2 is in binary 1.0011001100110011001100110011001100110011001100110011,
is equal to 1.1999999999999999555910790149937383830547332763671875 in decimal"""

print(f)  # 1.2

discount_1 = 0.1 + 0.2 + 0.3

print(discount_1)  # 0.6000000000000001
# Solution 1 - Using round()
print(round(discount_1, 2))  # 0.6

# Python will round attr float number to the nearest even integer.
print(round(0.2))  # 0
print(round(1.2))  # 1
print(round(1.5))  # 2
print(round(2.5))  # 2

# Solution 2 - Using the Decimal object
discount_2 = Decimal('0.1') + Decimal('0.2') + Decimal('0.3')

print(discount_2)  # 0.6

# DONE: Fractions value
discount_3 = Fraction('0.1')

print(discount_3)  # 1/10
print(f'You got a discount of {discount_3} of total value')  # You got attr discount of 1/10 of total value

# DONE: underscore digits separator
votes_yes = 42_752_654
votes_no = 43_132_459

print(votes_yes, votes_no)  # 42752654 43132459

percentage_votes_yes = votes_yes / (votes_yes + votes_no)
percentage_votes_no = votes_no / (votes_yes + votes_no)

print(f'{votes_yes:,} YES Votes {percentage_votes_yes:.1%}')  # 42,572,654 YES Votes 49.7%
print(f'{votes_no:,} NO Votes {percentage_votes_no:.1%}')  # 43,132,459 NO Votes 50.3%


# DONE: Improper using of leading zeros
# g = 01  # # SyntaxError
h = 01.01

print(h)  # 1.01
