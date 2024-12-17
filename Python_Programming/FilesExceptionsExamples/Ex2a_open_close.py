## Demonstrate reading from a file using open()

filename = 'pi_digits.txt'

file_object = open(filename, 'r')
#read() method: Returns the file content
contents = file_object.read()
print(contents)

#close the file when the access is done
file_object.close()
