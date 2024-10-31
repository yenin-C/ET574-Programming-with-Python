#Request an integer input, and then print whether the number is a multiple of 10 or not

number = input("Enter a number and I'll tell you if it's a multiple of ten ")

for num in number:
        
        if int(number) % 10 == 0:
                print(int(number + " is multiple of ten"))
else:
             if int(number) % 10 != 0:
                     print(int(number + ' is not multiple of 10'))

print()

#2. For & While
#a) Use a for loop to print all the numbers are even and multiples of 3 from 1 to 1000 inclusive.
pairs_multiples_of_3 = []
for number in range(1, 1001):
        if number % 2 == 0 and number % 3 == 0:
                pairs_multiples_of_3.append(number)

#b) Convert the for loop to a while loop
