#2

age = 34

if age < 0:
    print("Invalid age")
elif age < 2:
    print("You're a baby")
elif 2 <= age < 4:
    print("You're a toddler")
elif 4 <= age < 13:
    print("You're a kid")
elif 13 <= age < 20:
    print("You're a teenager")
elif 20 <= age < 65:
    print("You're an adult")
elif age >= 65:
    print("You're an elder")

print()

#Another example for No. 2

age = int(input ("Please tell me your correct age:"))

if age < 0:
    print("Invalid age")
elif age < 2:
    print("You\'re a baby")
elif age <= 4:
    print("You\'re a toddler")
elif age < 13:
    print("You\'re a kid")
elif age < 20:
    print("You\'re a teenager")
elif age < 65:
    print("You\'re an adult")
elif age <= 65:
    print("You\'re an elder")

#Another example
#2
age = int(input ("Please tell me your correct age:"))

if age < 0:
    print("Invalid age")
    age = int(input ("Please tell me your correct age:"))
elif age < 2:
    print("You\'re a baby")
    age = int(input ("Please tell me your correct age:"))
elif age <= 4:
    print("You\'re a toddler")
    age = int(input ("Please tell me your correct age:"))
elif age < 13:
    print("You\'re a kid")
    age = int(input ("Please tell me your correct age:"))
elif age < 20:
    print("You\'re a teenager")
    age = int(input ("Please tell me your correct age:"))
elif age < 65:
    print("You\'re an adult")
    age = int(input ("Please tell me your correct age:"))
elif age >= 65:
    print("You\'re an elder")

#I added the age input after each else if statement because I want it to loop until it reaches to an elderly age, once it reaches an elderly age, it will stop asking to enter your age.
print()

#3
usernames = ["brian", "admin", "vincent", "thomas", "george"]
user = 'admin'

if user:
    print(f"Hello {user.title()}, would you like to see a status report?.")

