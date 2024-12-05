## Demonstrate writing to a file

filename = 'C:\\Users\\student\\Downloads\\FilesExceptionsExamples\\programming.txt'
with open(filename, 'r') as file_object:
    print(file_object.read())

with open(filename, 'r+') as file_object:
    file_object.write("Hi Python\n")

with open(filename, 'w') as file_object:
    file_object.write("I loving programming.\n")
    file_object.write("I'm creating a new file.\n")

with open(filename, 'a') as file_object:
    file_object.write("Adding new text.\n")
    file_object.write("Adding more text.\n")

filename = 'newfile.txt'
with open(filename, 'x') as file_object:
    file_object.write("Are you ready for Python?\n")
