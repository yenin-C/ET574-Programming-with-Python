## Demonstrate the scope of variables

def my_function_1():
    ## Function definitions cannot be empty
    pass

def my_function_2():
    ## Demonstrate the function without parameters
    x = 123
    print("Hello " + str(x))

def my_function_3(x, y, z):
    ## Demonstrate the function with parameters and a return value
    print(f"Hello {x}, {y}, and {z}!")
    return x + y + z

def main():
    my_function_1()
    print()

    my_function_2()
    print()

    myNum = my_function_3(1, 2, 3)
    print("myNum =", myNum)
    print()

    print("myNum =", my_function_3(3, 2, 1))
    print()

main()
