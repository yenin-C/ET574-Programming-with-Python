## Demonstrate reading from a file using with

filename = 'pi_digits.txt'

#The keyword with closes the file once access to it is no longer needed.
#Python will close the file automatically when the with block finishes execution.
with open(filename) as file_object:
    #readline() method: Returns one line from the file

    contents = file_object.readline()
    #print(contents)
    '''
    x = file_object.readline()
    print(x)
    y = file_object.readline()
    print(y)
    z = file_object.readline()
    print(z)
    '''
    """
    for i in range(3):
        a = file_object.readline()
        print(a)
    """
print(contents)
