## Use modulo, % operator to setup conditions
## Use the return statement to generate a return value of a functions

# creating a function
def is_divisible(x, y):
    """function returning a boolean value"""
    return x % y == 0
    '''
    if x % y == 0:
        return True
    else:
        return False
    '''

# creating main() function
def main():
    print(is_divisible(6, 6))

# calling main() function to initiate the tasks to be performed
main()
