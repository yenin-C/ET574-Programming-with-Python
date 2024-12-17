## Demonstrate functions with multiple return values in a tuple

def main():
    # calling functions
    print(total(2, 3))
    print(total(2, 3, 4))
    print(total(2, 3, 4, 5))

    print(operations())
    print(operations(5, 4))


# define a function with return statement to generate a return value
def total(w, x, y=10, z=20):
    """function returning a numerical value"""
    return (w ** x) + y + z

# define a function with multiple return values in a tuple
def operations(x=1, y=1):
    return (x+y, x-y, x*y, x/y)


main()
