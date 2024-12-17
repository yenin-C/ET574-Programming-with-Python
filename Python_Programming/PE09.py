import math

while True:
    try:
        numerator = float(input('Enter the numerator: '))
        
        while True:
            denominator = float(input('Enter the denominator (Non Zero): '))
            if denominator != 0:
                break
            else:
                print('Denominator cannot be zero, please try again: ')
                
        remainder = math.fmod(numerator, denominator)
    
        print("The remainder is:", int(remainder))
        break

    except ValueError:
    
        print("Invalid input. Please enter numeric values.")
        
print()

#2. randint() & isqrt()

import random #This generates the random number for point a
import math 

number = random.randint(1, 101) #a) Use random module, randint() to generate a random number in the range (1, 100).

integer_square_root = math.isqrt(number) #b) Use math module, isqrt() to round a square root number downwards to the nearest integer.

#c) Print out the result.
print(f'Random Number: {number}')
print(f'Square Root: {integer_square_root}')

print()

#3. Write a function hello() that prints “Hello World” to the console. Implement the code to test the function.

def hello():
    print('Hello Professor! :)') #4. Modify the function, hello() above with a parameter.
    
hello()

#a) Define the function, helloNo(n) with a loop to call hello() n times to the console.   

def helloNo(n):
    for _ in range(n):
        hello()

#b) Use the parameter, n for the numbers of iterations in the loop. 
number_of_iterations = int(input('How many times do you want the message printed? '))
helloNo(number_of_iterations)

print() #OR:

#3. Write a function hello() that prints “Hello World” to the console. Implement the code to test the function.

def hello():
    print('Hello Professor! :)') #4. Modify the function, hello() above with a parameter.
    
hello()

#a) Define the function, helloNo(n) with a loop to call hello() n times to the console.   

def helloNo(n):
    n == 5
    for _ in range(n):
        hello()

#b) Use the parameter, n for the numbers of iterations in the loop.
helloNo(n=5)

print()

