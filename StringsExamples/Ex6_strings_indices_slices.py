# Chap2 - Variables
# String indices and slices
# J. Sun

print("Python")
print("Python"[0], "Python"[5], "Python"[:])
print()

str1 = "spam & eggs"
print(str1[1])
print(str1[2:7])
print(str1[7:2])      #produce the empty string if m>=n in str1[m:n]
print(str1[:4])
print(str1[7:])
print()

# negative indices and slices
print("Python")
print("Python"[-1], "Python"[-4], "Python"[-5:-2])
print()

str1 = "spam & eggs"
print(str1[-2])
print(str1[-8:-3])
print(str1[0:-1])
print()

# out of bounds
str1 = "Python"
print(str1[-10:10])
print(str1[-10:3])
print(str1[2:10])
print()

# Empty string
print('Empty string', str1[5:1])

#print(str1[7])       #IndexError: string index out of range
#print(str1[-7])      #IndexError: string index out of range
