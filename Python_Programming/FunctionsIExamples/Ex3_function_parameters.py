## Create user-defined function wtih parameters

# def function_name(parameter):
#   statement 1
#   statement 2
# print()
# function_name(parameter)

# creating a function
def my_function_1(p1):
    print("Hello " + p1)

# creating another function
def my_function_2(p1, p2):
    print()
    print(p1)
    print(p2)

# calling functions
my_function_1("World")
my_function_1('Python')
#my_function_1() #TypeError: missing required postional argument

my_function_2("Hi", "there" )
my_function_2(3.9, "python version")
#my_function_2() #TypeError: missing required postional argument
