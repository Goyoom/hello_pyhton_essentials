#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  September 3, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

String Built-in Methods and Functions."""

from time import asctime, sleep

# DONE: String Built-in Methods
print('Hello, World.'.lower())  # hello, world.
print('Hello, World.'.upper())  # HELLO, WORLD.
print('Hello, World.'.capitalize())  # Hello, world.
print('hello, world.'.title())  # Hello, World.
print('HELLO, world.'.swapcase())  # hello, WORLD.
print('Hello, World.'.center(17, '-'))  # --Hello, World.--
print('Hello, World.'.count('l'))  # 3
print('Hello, World.'.count('l', 0, 5))  # 2
print('Hello, World.'.replace(',', '.'))  # Hello. World.
print('  Hello, World. '.strip())  # Hello, World.
print('...Hello, World.'.rstrip('.'))  # ...Hello, World
print('John Peterson'.split())  # ['John', 'Peterson']
print('Hello.World'.rsplit('.'))  # ['Hello', 'World']
print('01.Johny.Peterson'.partition('.'))  # ('01', '.', 'Johny.Peterson')
print('Hello.World.'.startswith('h'))  # False
print('Hello.World.'.startswith('H'))  # True
print('Hello.World.'.endswith('.'))  # True
print('Hello.World.'.find('W'))  # 6
print('Hello.World.'.find('c'))  # -1
print('Hello.World.'.index('W'))  # 6

# DONE: String Built-in Functions
print(asctime())  # Thu Sep  3 14:44:35 2020
print(sleep(1), '....2 seconds passed')  # None ...2 seconds passed
print('Hello', 'World')  # Hello World
print('Hello', 'World', sep=', ')  # Hello, World
print('Hello', 'World', sep=', ', end='.\n')  # Hello, World.
print(len('Hello.World.'))  # 12
