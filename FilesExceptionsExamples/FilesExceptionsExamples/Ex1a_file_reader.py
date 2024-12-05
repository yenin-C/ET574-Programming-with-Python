## Demonstrate reading from a file using with

fileName = 'pi_digits.txt'
#fileName = 'C:\\myData\\text_files\\pi_digits.txt'
#fileName = 'G:\\myData\\text_files\\pi_digits.txt'

#The keyword with closes the file once access to it is no longer needed.
#Python will close the file automatically when the with block finishes execution.
with open(fileName) as file_object:
    #read() method: Returns the file content
    contents = file_object.read()

print(contents)
