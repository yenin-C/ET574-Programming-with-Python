## Use default numerical parameter value
## Use the return statement to generate a return value of a functions

# creating a function
def total(w, x, y=10, z=20):
    """function returning a numerical value"""
    return (w ** x) + y + z

# calling functions
print(total(2, 3))
print(total(2, 3, 4))
print(total(2, 3, 4, 5))
#print(total())  #TypeError:must enter p1 & P2
