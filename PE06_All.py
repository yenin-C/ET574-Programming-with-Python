# Number 1
a = 2
b = 3
c = 0
#A
print(a ** b == b ** a)
#Output: False, because 2 to the power of 3 is not the same as 3 to the power of 2
print()
#B
print(a < b or b < a)
#Output: True, because the first statement applies, 2 is less than 3, since this one is true it ignores the next statement
print()
#C
print('dog' > 'cat' + 'mouse')
#Output: 'cat' + 'mouse' concatenates into catmouse, therefore d comes after c, statement is True
print()
#D
print('Car' < 'Train')
#Output: 'C' in car comes before 'T' in train, statement is True that C is less than T
print()
#E
print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))
#Output: This is false because one of the conditions is false
print()
#F
print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b)))
#Output: This is true because the first condition is true 2 < 3
print()
#G
print(not ((a < b) and (a < (b + a))))
#Output: This is false because the condition is True but the 'not' at the beginning of the condition makes it false
print()
#H
print("small" > "large" and (not c ))
#Output: small is greater than large because 's' in small comes after 'l' in large, c is 0 which is considered False, but with 'not' it evaluates to True, both statements are True
print()
#I
print(isinstance(c, int))
#Output: The isinstance() function checks if an object (in this case, c) is an instance or subclass of a specified class or tuple of classes (in this case, int(eger)). C is an integer therefore is True
print()
#J
print(isinstance(3.14, float))
#Output: Is checking to see if 3.14 is a float, it is indeed a float
print()
#K
if (a < b < c):
    b = c + a
else:
    b = c * a
print(b)
#Output: Since the first statement is False, because 2 + 0 does not equal 3, the else statement applies, which is 2 * 0 = 0
print()
#L
if ('A' in 'apple'):
    print("A as apple." )
else:
    print('Oops, not there.')
#Output: Python is case sensitive, the string 'apple' does not have A in it
print()
#M
x = 6
if (x < 0):
    print('negative')
else:
    if (x == 0):
        print('zero')
    else:
        print('positive')
#Output: Positive because 6 is neither <= 0
print()
#N
n = 1
if n <= 9:
    print ("Less than ten.")
elif n == 1:
    print("Equal to one.")
#Output: 1 is less than ten, first statement is true
print()
#O
let = input("Enter A, B or C: \n")
let = let.upper()
if (let == 'A'):
    print('\nA, my name is Alice.')
elif (let == 'B'):
    print('\nTo be, or not to be.')
elif (let == 'C'):
    print('\nOh, say, can you see.')
else:
    print('\nInvalid letter.')
#Output: prompts the user to enter any letter and depending on which a different message appears
print()
# Number 2
#Write an if-elif-else chain that determines a person’s stage of life.
#a) Set your age for the variable age.
age = int(input ("Please tell me your correct age:"))
#b) If the age is less than 0, print an error message, invalid age.
if age < 0:
    print('Invalid Age')
    age = int(input ("Please tell me your correct age:"))
#c) If the age is less than 2 years old, print a message, you’re a baby.
elif age < 2:
    print('You\'re a baby')
    age = int(input ("Please tell me your correct age:"))
#d) If the age is at least 2 years old but less than 4, print a message, you’re a toddler.
elif age == 2 and age < 4:
    print('You\'re a toddler')
    age = int(input ("Please tell me your correct age:"))
#e) If the age is at least 4 years old but less than 13, print a message, you’re a kid.
elif age >= 4 and age < 13:
    print('You\'re a kid')
    age = int(input ("Please tell me your correct age:"))
#f) If the age is at least 13 years old but less than 20, print a message, you’re a teenager.
elif age >= 13 and age < 20:
    print('You\'re a teenager')
    age = int(input ("Please tell me your correct age:"))
#g) If the age is at least 20 years old but less than 65, print a message, you’re an adult.
elif age >= 20 and age < 65:
    print('You\'re an adult')
    age = int(input ("Please tell me your correct age:"))
#h) If the age is 65 or older, print a message, you’re an elder.
elif age >= 65:
    print('You\'re an elder')
    age = int(input ("Please tell me your correct age:"))
print()   
# Number 3
#Implement the following to print a greeting to each user after they log in to a website.
#a) Make a list of five usernames, including the name “admin”.
#b) Loop through the list and print a greeting to each user.
#c) If the username is “admin”, print a special greeting, such as
#Hello Admin, would you like to see a status report?
#d) Otherwise, print a generic greeting, such as
#Hello Eric, thank you for logging in again!
#e) Implement if the list is empty by printing the message, We need to find some users.
usernames = ["brian", "vincent", "thomas", "george"]
user = input("What is your username?: ")

if not usernames:
    print("We need to find some users.")
else:
    
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    
    elif user in usernames:
        print(f"Hello {user.title()}, thank you for logging in again!")
print()
#Number 4

#Implement the following to simulate how websites ensure that everyone has a unique username.
#a) Make a list of five or more usernames called current_users.
#b) Request an input of username.
#c) Print a message, Sorry xxx, that name is taken and also display the current user list if the input
#username has already been used. xxx is the input user name.
#d) Print a message, Great, xxx is still available and also display the updated user list if the username has not been used.
#e) Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' or ‘john’ should not be accepted.
#Usernames must be at least 3 characters long <--- Extra challenge to make it look more real ;p

current_users = ["bob", "yenin", "charlie", "nurys", "josh"]

while True:
    new_username = input("Enter a new username (minimum 3 characters): ")

    if len(new_username) < 3:
        print("Sorry, the username must be at least 3 characters long.")
    else:
        
        if new_username.lower() in [user.lower() for user in current_users]:
            print(f"Sorry {new_username}, that name is taken.")
            print("Current user list:", current_users)
        else:
           
            current_users.append(new_username)
            print(f"Great, {new_username} is still available!")
            print("Updated user list:", current_users)
            break
print()        
#Number 5
#a) Create a list named vehicles: car, Truck, boat, PLANE.
vehicles = ["car", "Truck", "boat", "PLANE"]
#b) Request a user input for a search letter.
search_by_letter = input("Enter a letter to search for: ")
#e) Print the error message if more than one letter is entered.
if len(search_by_letter) != 1:
    print("Error: Please enter only one letter.")
#c) Use the decision structure in a for loop to search all the items which contains the input letter (ignoring case) in the list
else:
      found = False #Set flag to False if a match is not found
      for index, vehicle in enumerate(vehicles):
        # Check if the search letter is in the current vehicle (case insensitive, must add .lower)
        if search_by_letter.lower() in vehicle.lower():
            found = True  # Set flag to True if a match is found
            # Step d: Print the item and its position
            print(f"Found '{search_by_letter}' in '{vehicle}' at position {index}.")
    
    # If no matches were found, print a message
if not found:
        print(f"No vehicles contain the letter '{search_by_letter}'.") 
        
#Number 6
#Identify the errors and rewrite the statement in the correct syntax

# A
n = eval(input("Enter a number: "))
#if n = 7: 'an additional = sign'
if n == 7:
#print("The square is", n*2) 'indentation'
    print("The square is", n*2)   
    
# B
#n = 6
#if n > 5 and < 9: 'n'
#print("Yes")
#else:
#print("No") 'indentation'
n = 6
if n > 5 and n < 9:
    print("Yes")
else:
    print("No") 
    
# C
major = "Computer Science"
if major == "Engineering Technology" or "Computer Technology": #Capitalized O in or, and missing colon
    print("Yes") #indentation
    
# D

a, b = 1, 1.0
if a == b: #missing additional = because it's a comparison, not a variable
    print("same")
