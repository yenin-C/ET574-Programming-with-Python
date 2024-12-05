NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}

#A:
print((NY['QS']))
print(NY.get("QS"))
#Prints/gets 2.25 which is the key value for QS in the dictionary

#B:
print(NY.get("LI", "Not in"))
print(NY.get('SI', 'absent'))
print(NY.setdefault('SI', 0.48))

#C:
print("LI" in NY)
print('MN' not in NY)

#D:
print(len(NY), min(NY), max(NY))
print(len(NY.items()),
max(NY.keys()), min(NY.values()))

#E:
print(round(NY['QS']))
NY['QS'] += .3
print(round(NY['QS'], 1))

#F:
print(NY.keys())
print(list(NY.values()))
print(tuple(NY.items()))

#G:
total = 0
for x in NY.values():
    total += x
print(f'{total:.1f}')

#H:
total = 0
for x in NY:
    total += NY[x]
print(f'{total:.1f}')

#I:
for x in sorted(NY):
    print(x, end = '|')

#J:
#Use a for loop to print all key names in the reversed alphabetical order (see output below).
# SI|QS|MN|BX|BN|
NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}

for city in sorted(NY.keys(), reverse=True):
    print(city, end='|')



#K:
#Use a for loop to print all values from max to min order (see output below).
# 2.56, 2.25, 1.63, 1.42, 0.47
for value in sorted(NY.values(), reverse=True):
    print(value, end=', ')


#L:
if "QS" in NY:
    print("Queens is the most diverse county in NY.")
#If the key "QS" is in the dictionary NY, then print the message
    
    
    
#M:
for x, y in NY.items():
    if y > 2.5: print(f"{x} is the Kings county!")

#N:
NY["SK"] = 1.49
print(NY)


#O:
NY.update({"NU":1.34})
print(NY)


#P:
NY.pop("QS")
NY.popitem()
print(NY)


#Q:
newYork = NY
del newYork['BN']
print(NY)
print(newYork)


#R:
newYork = dict(NY)
del newYork["BN"]
print(len(NY))
print(len(newYork))


#S:
NewYork = NY.copy()
NY.clear()
print(NY)
print(NewYork)
del NY
print(set(NewYork))


# 2:
#Convert the following two lists into one dictionary:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Example Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dictionary = dict(zip(keys, values))
print(dictionary)

# 3:
#Merge the following two dictionaries into one dictionary:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

#Example Output: {‘Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

# 4:
#Create a dictionary and use loops to print keys and values:
#a) Create a dictionary, stuInfo with the keys name, gpa, and age. Give appropriate values for each key.
stuInfo = {"name": "Steven", "gpa": "3.0", "age": "27"}

#b) Use a loop and the items() method to print all keys and values.
for x, y in stuInfo.items():
    print(x, y)
#c) Use the update() method to change the gpa to 4.0.
stuInfo.update({"gpa": "4.0"})
#d) Use a loop and the keys() method to print all keys and values.
for z in stuInfo.keys():
    print(z, stuInfo[z])
#e) Add a key major with the value to the dictionary.
stuInfo.update({"major": "cybersecurity"})
#f) Use a loop and the values() method to print all values.
for x in stuInfo.values():
    print(x)
#g) Use two different ways to delete gpa and age in the dictionary.
stuInfo.pop("gpa")
del stuInfo["age"]
#h) Print the updated dictionary.
print(stuInfo)

# 5:
#Displays a rank in the defined dictionary.
#a) Create a dictionary, rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
#b) Request a user input for a number of years.
try:
    r = int(input("Enter the number of years in the school (1-4): "))
#c) Print the value of the matching key in the dictionary.
    if 1 <= r <= 4:
        print(f"Year {r}: {rank[r]}")
    else:
        print("Error: Please enter a number between 1 and 4.")   
#d) Print the error message if input is invalid.
except ValueError:
    print("Error: Invalid input. Please enter a valid number between 1 and 4.")

# 6:
#Nest dictionaries within a list, stuClass.
#a) Create three stuInfo dictionaries with the keys: name and value: gpa. Add appropriate values for each key.
stuInfo1 = {"name": "Vincent", "gpa": 3.0}
stuInfo2 = {"name": "Steven", "gpa": 2.8}
stuInfo3 = {"name": "Charlie", "gpa": 3.9}
#b) Create a list stuClass, add all dictionaries to this list, and print the list.
stuClass = [stuInfo1, stuInfo2, stuInfo3]
print(stuClass)
print()
#c) Use a loop to print all students from the list of stuClass.
for index, student in enumerate(stuClass, start=1):
    print(f"Student {index}: {student['name']} \t GPA: {student['gpa']}")
print()
#d) Use a loop to print all the gpa.
for student in stuClass:
    print(student["gpa"], end= '|')
print()
#e) Change the last student’s gpa to 4.0.
stuClass[-1]["gpa"] = 4.0
#f) Add a new student info to the list.
new_student = {"name": "Joshua", "gpa": 3.5}
stuClass.append(new_student)
#g) Use a loop to print all the names and gpa with proper format as the output below.
print()
for student in stuClass:
    print(f"Name: {student['name']} \t GPA: {student['gpa']}")   


# 7a:
#Implement the following:
#a) Use a for loop to create a list with 26 letters (a-z).
alphabet = []
for i in range(26):
    letter = chr(i + ord('a'))
    alphabet.append(letter)
#b) Use a for loop to create a list with 26 numbers from 1 to 26 inclusive.
numbers = []
for z in range(1, 27):
    numbers.append(z)
#c) Create a dictionary, charNum by zipping above two lists.
charNum = dict(zip(alphabet, numbers))
#d) Use a for loop to print the keys and values in the dictionary as the output below
for key, value in charNum.items():
    print(f"{key} {value}", end='|')

# 7b:
#Implement the following:
#a) Use a for loop to create a list with 26 letters (A-Z).
letters = []
for i in range(26):
    letter = chr(i + ord('A'))
    letters.append(letter)
#b) Use a for loop to create a list with 26 numbers from 100 to 2600 (with step value of 100) inclusive.
values = []
for y in range(100, 2601, 100):
    values.append(y)
#c) Create a dictionary, numChar by zipping above two lists.
numChar = dict(zip(letters, values))
#d) Use a for loop to print the keys and values in the dictionary as the output below.
for key, value in numChar.items():
    print(f"{value} {key}", end='|')
print()
#e) Merge the dictionary, charNum created in 7a with the dictionary, numChar into one dictionary, all.
all = {
    "charNum": charNum,
    "numChar": numChar
}
#f) Print out the dictionary, all as the output below.
print(all)
