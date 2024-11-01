# a
number = input("Enter a number and I'll tell you if it's a multiple of ten ")

for num in number:
        
        if int(number) % 10 == 0:
                print(int(number + " is multiple of ten"))
else:
             if int(number) % 10 != 0:
                     print(int(number + ' is not multiple of 10'))

#Fixed Code

number = input("Enter a number and I'll tell you if it's a multiple of ten: ")

# Convert the input to an integer
try:
    number = int(number)  # Attempt to convert to integer

    # Check if the number is a multiple of ten
    if number % 10 == 0:
        print(f"{number} is a multiple of ten.")
    else:
        print(f"{number} is not a multiple of ten.")
except ValueError:
    print("Please enter a valid number.")




# b
numbers = []
for number in range(1, 101):
    numbers.append(number)
print(sum(numbers))
