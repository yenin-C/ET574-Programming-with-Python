# 1. File Reading
#There are names of the first three U.S. presidents in the file, Presidents.txt. Create functions to read and display the contents of the file in the following two ways.

#Using Loop:
filename = 'C:\\Users\\student\\Downloads\\FilesExceptionsExamples\\USPres.txt'
with open(filename) as file_object:
    count = 0
    for line in file_object:
        print(line.rstrip())
        count += 1
        if count == 3:
            break

print('\n')

#Using List:
with open(filename) as file_object:
    lines = file_object.readlines() #This reads all lines in the list
for line in lines[:3]:  # Slice the list to get the first three lines
    print(line.rstrip())

#2. File Writing
#Write a program that defines two different functions to create files
filename = 'Sample3.txt'
with open(filename, 'x') as file_object:
    file_object.write("George Washington\n")
    file_object.write("John Adams\n")

print('\n')

#3. File Appending
#Write a program that adds/appends lines to the end of an existing file
filename = 'Sample3.txt'
with open(filename, 'a') as file_object:
    file_object.write("Thomas Jefferson.\n")
    file_object.write("James Madison.\n")
    file_object.write("James Monroe.\n")
    file_object.write("John Quincy Adams.\n")
#Open File Created
filename = 'Sample3.txt'
file_object = open(filename, 'r')
#read() method: Returns the file content
contents = file_object.read()
print(contents)


