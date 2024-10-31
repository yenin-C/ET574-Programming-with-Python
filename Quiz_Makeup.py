# a
number = input("Enter a number and I'll tell you if it's a multiple of ten ")

for num in number:
        
        if int(number) % 10 == 0:
                print(int(number + " is multiple of ten"))
else:
             if int(number) % 10 != 0:
                     print(int(number + ' is not multiple of 10'))




# b
numbers = []
for number in range(1, 101):
    numbers.append(number)
print(sum(numbers))