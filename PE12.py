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

