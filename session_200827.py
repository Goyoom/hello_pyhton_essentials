#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  August 27, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Strings."""

# TODO: Strings
word = 'Python'

print(word)  # Python
print(word[0])  # P
print(word[0:2])  # Py
print(word[1:])  # ython
print(word[-1])  # n
print(word[:-1])  # Python
print(word[-3:])  # hon
print(word[-4:-1])  # tho
print('Python'[-1])  # n

# TODO: Strings Iteration
# word = 'Python'
#
# for letter in word:
#     print(letter)


# TODO: Strings Concatenation
# print('Hello, ' + 'World!')  # Hello, World!
# print('Hello, ' 'World!')  # Hello, World!


# TODO: Strings Repetition
# print('Mew! ' * 3)

# TODO: Strings Formatting with .format()
# print('Employee {}{}'.format('No.', 42))  # Employee No.42

# TODO: Strings Positional Arguments with .format()
# print('Employee {prefix}{number}'.format(prefix='No.', number=42))  # Employee No.42
# print(
#     'Python {0} {1} and {1} {0} awesome!'.format('is', 'fun')
# )  # Python is fun and fun is awesome!
#
# template = """
# From: <{from_email}>
# To: <{to_email}>
# Subject: {subject}
#
# {message}
# """
#
# print(
#     template.format(
#         from_email="sender@domain.com",
#         to_email="recipient@domain.com",
#         subject="Hello!",
#         message="Here's some mail for you. " " Hope you enjoy the message!",
#     )
# )

# From: <sender@domain.com>
# To: <recipient@domain.com>
# Subject: Hello!

# Here's some mail for you.  Hope you enjoy the message!

# TODO: Strings Control Alignment with .format()
# print('{0:9} | {1:8}'.format('Vegetable', 'Quantity'))
# print('{0:9} | {1:8}'.format('Asparagus', 3))
# print('{0:9} | {1:8}'.format('Onions', 10))

# Vegetable | Quantity
# Asparagus |        3
# Onions    |       10

# print('{0:9} | {1:<8}'.format('Vegetable', 'Quantity'))
# print('{0:9} | {1:<8}'.format('Asparagus', 3))
# print('{0:9} | {1:<8}'.format('Onions', 10))

# Vegetable | Quantity
# Asparagus | +3
# Onions    | 10

# TODO: Strings Control Padding with .format()
# print('{}{:03}'.format('No.', 2))  # No.02
# print('{}{:02}'.format('No.', 12))  # No.12

# TODO: Unicode Characters
# emoji = '\U0001f600'
#
# print('Hello {}!'.format(emoji))  # Hello 😀!

# TODO: Lists and Tuples Concatenation
# letters_1 = ['a', 'b', 'c']
# letters_2 = ['d', 'e', 'f']
#
# numbers_1 = 1, 2, 3
# numbers_2 = 4, 5, 5
#
# print(letters_1 + letters_2)
# print(numbers_1 + numbers_2)
