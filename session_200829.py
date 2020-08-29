#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  August 27, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Strings."""

# Done: F-Strings
number = 42
log1 = f'Employee No.{number}'
log2 = f'Employee No.{number:03d}'

print(log1)
print(log2)

# Done: F-Strings Conversions
name = 'John'

print(f'His name is {name!s}')  # His name is John (default)
print(f'His name is {name!r}')  # His name is 'John' (equal to His name is name.__repr__())
print(name.__repr__())  # 'John'

# Done: Characters Escaping
print("His name is 'John'")  # His name is 'John'
print('His name\nis \'John\'')  # His name is 'John'

# Done: R-Strings
print(r'C:\path\to\file')  # C:\path\to\file

# r-strings cannot end with '\' backslash, to solve this:
print(r'C:\path\to\file' '\\')  # C:\path\to\file\
print(r'C:\path\to\file\ '[:-1])  # C:\path\to\file\
# print('C:\path\\to\\file\\')  # C:\path\to\file\ (less readable)

# Done: Combining F-Strings With R-Strings
ext = 'jpg'

print(fr'C:\path\to\file.{ext}')  # C:\path\to\file.jpg
