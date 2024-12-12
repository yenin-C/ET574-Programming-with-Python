import os

filename = 'creating_a_new_file.txt' #File name could be anything
base, ext = os.path.splitext(filename)
counter = 1 #This is the increment of the number in the file i.e.: 'creating_a_new_file_1.txt' in case original name already exists

while os.path.exists(filename):
    filename = f"{base}_{counter}{ext}"
    counter += 1

with open(filename, 'x') as file_object:
    file_object.write("I am creating a file\n")

    print(f"File created with name: {filename}")



#This can also be done by using functions

import os

def create_new_file(filename):
    base, ext = os.path.splitext(filename)
    counter = 1

    while os.path.exists(filename):
        filename = f"{base}_{counter}{ext}"
        counter += 1
    return filename

filename = 'UN.txt'
unique_filename = create_new_file(filename)

with open(unique_filename, 'x') as file_object:
    file_object.write("This is some new content\n")

print(f"File created with name: {unique_filename}")
