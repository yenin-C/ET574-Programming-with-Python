#Use a for loop on the file object to examine each line from a file one at a time

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
