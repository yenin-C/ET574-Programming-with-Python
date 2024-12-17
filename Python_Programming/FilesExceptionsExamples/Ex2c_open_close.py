## Demonstrate reading from a file using open()

filename = 'pi_digits.txt'

file_object = open(filename, 'r')
#readlines() method: Returns a list of lines from the file
contents = file_object.readlines()
print(contents)

for line in contents:
    print(line.rstrip())

file_object.close()     #close the file
