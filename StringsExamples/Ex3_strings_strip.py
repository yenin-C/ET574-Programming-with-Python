# Chap2 - Variables
# Using string methods to remove space in strings
# S. Trowbridge/J.Sun


fruits = "      apples & pears      "
#fruits = fruits.rstrip()
#fruits = fruits.lstrip()
print("0123456789012345678901234567890123456789")
print(fruits)

# note the additional whitespace
print(fruits+" are delicious.\n")

# rstrip removes white space from the RIGHT side of the string for the print command
print(fruits.rstrip()+" are delicious.\n")

# note that rstrip did not change the value of the variable name
print(fruits+" are delicious.\n")

# lstrip removes white space from the LEFT side of the string for the print command
print(fruits.lstrip()+" are delicious.\n")

# note that lstrip also does not change the value of the variable name
print(fruits+" are delicious.\n")

# chain the two methods
print(fruits.strip().capitalize()+" are delicious.\n")
