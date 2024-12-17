## Demonstrate reading from a file using with

filename = 'pi_digits.txt'

#The keyword with closes the file once access to it is no longer needed.
#Python will close the file automatically when the with block finishes execution.
with open(filename) as file_object:
    #readlines() method: Returns a list of lines from the file
    lines = file_object.readlines()
print(lines)

for line in lines:
    #rstrip() method: Remove any white spaces at the end of the string
    print(line.rstrip())
    #print(line)
