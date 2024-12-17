## Use modulo, % operator to setup conditions
## Use the return statement to generate a return value of a functions

# creating a function
def is_divisible(x, y):
    """function returning a boolean value"""
    return x % y == 0

# creating main() function
def main():
    #implement the exception handling
    try:
        print("Divisible = ", is_divisible(6, 12))
    except:
        print("Exception: ZeroDivisionError")

# calling main() function to initiate the tasks to be performed
main()
