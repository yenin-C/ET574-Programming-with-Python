'''
1. Print List
a) Define a function printList() with one parameter p.
1) This function prints all values in the list p.
b) Define a main() function to do the following:
1) Create a list of strings called lst. For example, lst = [“apple”, “banana”, “cherry”].
2) Call the function printList() with lst as an argument.
c) Call main() function to initiate the tasks to be performed
'''
def printList(p):
    for item in p:
        print(item)
        
def main():
    lst = ["oatmeal", "chicken sandwich", "corn flakes", "coffee or tea"]
    printList(lst)
    
main()

print("\n")

'''
4. Print Arbitrary Values
a) Define a function printNames() with a parameter names.
The names parameter builds a tuple of any number of argument values.
This function prints all contents of the names tuple.
b) Call the function printNames() with any number of name arguments
'''
def printNames(*names):
    for name in names:
        print(name)        

printNames("Nurys", "Joan", "Susan", "Gaby", "Ashley")

print("\n")

'''
5. Dictionary
a) Define a function createUser() with an arbitrary dictionary parameter.
This function returns a dictionary based upon input arguments.
b) Define a function printUser() with a parameter user which is a dictionary.
This function prints the contents of the dictionary user.
c) Create and print the user: John, age 43, job Programmer, Hobby Biking
d) Create and print the user: Sara, age 20, school QCC, major CSIS
'''
def createUser(**usuario):
    return usuario

def printUser(user):
    for first, last in user.items():
        print(f"{first}: {last}")
        
def main():
    John = createUser(name="John", age = 43, job = "Programmer", hobby = "Biking")
    print("User John:")
    printUser(John)
    print("\n")
    
    Sara = createUser(name = "Sara", age = 20, school = "QCC", major = "CSIS")
    print("User Sara:")
    printUser(Sara)
    
main()

print("\n")

'''
6. Averaging
a) Define a function average() with a parameter grades that can accept an arbitrary number of integer values.
This function returns the average of all values.
b) Define a main() function to do the following:
1) Call the average() function with the following arguments: 95,87,83,74
2) Create two random integers, x and y. x is from range -100 to 0, and y is range from 0 to 100 inclusively.
3) Call the average() function with x and y.
4) Print al the results with the average computed to two decimal places.
c) Call main() function to initiate the tasks to be performed        
'''
import random

def average(*grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def main():
    avrg1 = average(95, 87, 83, 74)

    x = random.randint(-100, 0)
    y = random.randint(0, 100)

    avrg2 = average(x, y)

    print(f"Average of 95, 87, 83, 74: {avrg1:.2f}")
    print(f"Random integers: x = {x}, y = {y}")
    print(f"Average of x and y: {avrg2:.2f}")    

main()