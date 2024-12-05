#Excercise 1

#Request an integer input, and then print whether the number is a multiple of 10 or not
number = input("Enter a number, and I'll tell you if it's a multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")
    
    print()
    
#Excercise 2

#a) Use a for loop to print all the numbers are even and multiples of 3 from 1 to 1000 inclusive.
Even_Numbers = []
for number in range(1, 1001):
    if number % 2 == 0 and number % 3 == 0:
        Even_Numbers.append(number)
        print(Even_Numbers, end = '')
print()
#b) Convert the for loop to a while loop.
Even_Num = [] 
i = 2 
while i <= 1000:
    if i % 3 == 0:
        Even_Num.append(i)
    i += 2        
print(Even_Num, end = '')

print()

#Excercise 3

#a) Use a for loop to calculate and print the sum of all numbers between 1 to 100 inclusive.
numbers = []
for number in range(1, 101):
    if number % 2 == 0:
        numbers.append(number)
print(sum(numbers))
#b) Use a while loop to calculate and print the sum of all even numbers between 1 to 100 inclusive.
numbers = 1
total_sum = 0
while numbers <= 100:
    if numbers % 2 == 0:
        total_sum += numbers
    numbers += 1

print(total_sum)
print()

#Excercise 4

#Use a loop to print all the numbers are odd and multiples of 5 from 1 to n inclusive
#n is a user input
number = input("Enter a number n: ")
#b) Implement (an if-else) statements to validate n.
if number.isdigit(): #The code first checks if the input consists only of digits using isdigit(), which ensures the input is a positive integer.
    n = int(number) #If the input is a valid positive integer, it converts it to an integer.
    if n <= 0: #If the input is not a valid number or if n is less than or equal to 0...
        print("Invalid input. Please enter a positive integer. ") #...it prints an error message.
    else:
        print(f"Odd multiples of 5 from 1 to {n}:")
        for i in range(1, n + 1):  # Loop from 1 to n
            if i % 2 != 0 and i % 5 == 0:  # Check if odd and a multiple of 5
                print(i)  # Print the number
else:
    print("Invalid input. Please enter a positive integer.")

print()

# Excercise 5

#a) Implement a while loop to print all the numbers from 9 to 1 inclusive.
backwards_count = 10
while backwards_count < 11:
    backwards_count -= 1
    if backwards_count == 0:
        break
    print(backwards_count)
#b) Then display Happy New Year!   
print('Happy New Year!')
#c) Convert the while loop to a for loop
start = 9
end = 0
for i in range(start, end, -1):
    print(i)
    
print('Happy New Year!')
print()

#Excercise 6

import random #The import random statement is used to include the random module in your Python program. This module provides functions to generate random numbers and perform random operations.
# a) Request an integer input for the number of grades in the list
numberofgrades = int(input("Enter the number of grades: "))
# b) Use a loop to generate random grades (1 – 100) in the list, grades
grades = []
for _ in range(numberofgrades):
    grades.append(random.randint(1, 100))
# c) Request a user input for the passing grade
passing_grade = int(input("Enter the passing grade: "))
# d) Use a loop to store all the passing grades into a new list, passGrades
passGrades = []
for grade in grades:
    if grade >= passing_grade:  #Check if the grade is passing
        passGrades.append(grade)  #Add to the passGrades list
# e) Print all the lists
print("Grades:", grades)
print("Passing Grades:", passGrades)
print()

#Excercise 7

#a) Implement a while loop to request numbers from the console and insert them into a list.
#b) Insert all the numbers into a list.
number = []
prompt = int(input('Please enter a number, zero to stop: '))
while prompt != 0:
    number.append(prompt)
    prompt = int(input('Please enter a number, zero to stop: '))
    print(number, end = '')
    prompt = int(input('Please enter a number, zero to stop: '))
#c) Stop requesting values if the user input is a zero (0).
if prompt == 0:
    number.append(prompt)
#d) Print all elements of the list, sum and average.
if len(number) > 0:
        average = sum(number) / len(number)
        print(sum(number))
        print("Average of the grades:", average)
else:
        print('No numbers entered')
print()        

#Excercise 8

# a) Request two numbers, n1 and n2 from the console
n1 = int(input('Please enter the first number (n1): '))
n2 = int(input('Please enter the second number (n2): '))

# c) Use a while loop to print n1 to n2 with increment by 1 if n1 is smaller than n2
if n1 < n2:
    print(end=' ')
    while n1 <= n2:
        print(n1, end=' ')
        n1 += 1
    print()  # New line after printing

# d) Use a for loop to print n1 to n2 with decrement by 1 if n1 is greater than n2
elif n1 > n2:
    print(end=' ')
    for i in range(n1, n2 - 1, -1):
        print(i, end=' ')
    print()  # New line after printing

# e) Print a message if n1 is equal to n2
else:
    print("n1 = n2")
print()

#I could not get the secuential order of the numbers for C and D
#a) Request two numbers, n1 and n2 from the console.
#n1 = int(input('Please enter the first number n1: '))
#n2 = int(input('Please enter the second number n2: '))
#b) n1 and n2 can be any integer value.
#c) Use a while loop to horizontally print n1 to n2 with increment by 1 if n1 is smaller than n2.
#while n1 < n2:
#    print(n1 + 1, end = '')
#    print()
#    break
#if n1 == n2:
#    print("n1 is equal to n2")
#d) Use a for loop to horizontally print n1 to n2 with decrement by 1 if n1 is greater than n2.
#n1 = int(input('Please enter the first number n1: '))
#n2 = int(input('Please enter the second number n2: '))
#if n1 > n2:
#    for i in range(n2):
#        print(n1 - 1, end=' ')
#e) Print a message, “n1 = n2” if n1 is equal to n2.
#else:
#    if n1 == n2:
#        print("n1 is equal to n2")
#print()



#Excercise 9
#a) Request the lower bound, lower and the upper bound, upper from the console.
lower = int(input('Please enter a lower bound: '))
upper = int(input('Please enter an upper bound: '))
#b) Request an increment value incVal from the console.
incVal = int(input('Enter a number to increment by: '))
#c) Use a while loop to increment from lower to upper by increments of incVal (see example output below).
increment = lower
while increment <= upper:
    print(increment, end = ' ')
    increment += incVal
print()
#For example, with increment of 3, the program will output 0 3 6 9 12, given lower of 0 and upper of 12.
#d) Use a while loop to vertically print all values in between each increment.
print('Values between each increment')
increment = lower
while increment <= upper:
    print(increment)
    increment += incVal
#e) Use a for loop to vertically print all values in between each increment.
for n in range(lower, upper, incVal):
    print(n)
    