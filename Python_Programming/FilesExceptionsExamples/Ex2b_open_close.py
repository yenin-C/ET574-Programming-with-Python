## Demonstrate reading from a file using open()

filename = 'pi_digits.txt'

file_object = open(filename, 'r')
#readline() method: Returns one line from the file
contents = file_object.readline()
print(contents)

file_object.close()     #close the file
