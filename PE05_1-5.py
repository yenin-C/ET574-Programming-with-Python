#1: A – D, determine the output displayed by the lines of code. E – G, write the codes by using the output

#A
a = list(range(5))
print(a)
#Prints a list of 5 objects in a list, in this case a sequence of numbers that go from 0 to 4.

#B
b = []
for i in range (5):
    b.append(i)
print(b)
#First we have an empty list, then we add items, in this case integers at the end of the list that go from 0 to 4, for a total of 5 items

#C
x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))
#In here we have a range of numbers between -10 and 9 inclusive. It then prints the minimum integer, the maximum integer, and the nwe have the sum of all the integers in the list

#D
even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])
#This creates a sequence of numbers from 0 to 11 every 2 digits, then it prints the even numbers and accesses the first even number of the list which is 2 and the last even number on the list which is 10
print()

#E
#Print all the odd numbers from 1 to 9 inclusive in a list, odd_num:
odd_num = list(range(1, 10, 2)) #create a list from 1 to 10 (-1) in step of 2
print(odd_num) #prints all the odd numbers in the list

#F
#Make a list of the first 10 cubes and use a for loop to print out the value of each cube in a new line
cubes = [y**3 for y in range(1, 11)] #y**3 is what elevates the number to the cube
for cube in cubes:
    print(cube)
    
#G
#Use a list comprehension to generate a list of the first 10 cubes. Use a for loop to print out the value of each cube in a row separated by a ‘|’
cubes = [z**3 for z in range(1, 11)]
for cube in cubes:
    print(cube, end = '|')

print()
print()
#2: List slicing

#Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive:
even_numbers = [g for g in range(0, 101) if g % 2 == 0]
print(even_numbers)

#Use slicing to print the first five even numbers in the list:
print(even_numbers [:5])

#Use slicing to print the last five even numbers in the list:
print(even_numbers[-5:])

#Use slicing to print all list numbers between 20 and 30 inclusive:
print(even_numbers[10:16])
print()

#3: Lists, comprehensions, loops and slicing

#Create a list comprehension of multiples of 4 from 0 to 10 inclusive: (4 multiplied by all the numbers from 0 to 10)
multiples_of_4 = [i for i in range(0, 41) if i % 4 == 0]
print(multiples_of_4)
print()

#Create an empty list
this_is_an_empty_list = []

#Use a loop to insert all elements from the first list to the second list:
for element in multiples_of_4:
    this_is_an_empty_list.append(element / 2) #Before storing into the new list, divide each copied element by 2
    print(this_is_an_empty_list)
    print()
    
#Use slicing to copy the second list to a new third list
third_list = this_is_an_empty_list[:]
print(third_list)
print()

#Use a loop to divide and store each element of the third list by 2
divided_list = []
for element in third_list:
    divided_list.append(element / 2)
    print(divided_list)
    print()
    
#4: Implement the code that replaces the name of each month with its three-letter abbreviation

#Create a list below and print it out
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
print(months)
#Use a for loop to store each month with its first three-letter abbreviation into a new list. Print the value of each month in uppercase separated by a ‘|’ in a row as displayed in the example output
months_abbr = []
for month in months:
    abbr = month[:3] #This will get the first three letters
    print(abbr.upper(), end = '|')

print()
print()

#5: Implement the following to create a list and produce the multiplication table

#Request an integer input range
number = 7

size = 10

#Implement a list of the numbers 1 to range inclusive

for i in range(1, size + 1):
    print(f"{number} x {i} = {number * i}")
    
    print()
    
    # Get input from the user
number = int(input("Enter a number to get its multiplication table: "))

# Define the range for the multiplication table
size = 10

# Print the multiplication table for the input number
for i in range(1, size + 1):
    print(f"{number} x {i} = {number * i}")

for i in range(1, 4):
    print(f"{i}\t{2**i}")    
    