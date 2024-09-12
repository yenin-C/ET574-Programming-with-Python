# Chap2 - Variables
# string methods
# J. Sun

str1 = "spam & eggs"
print(str1.index('&'))      # Returns the index # of the first position of where the search item was found
#print(str1.index('+'))     # Returns ValueError if the search item was not found
print(str1.find('a'))       # Returns the index # of the first position of where the search item was found
print(str1.find('b'))       # Returns the -1 if the search item was not found
print(str1.find('s'))       # Returns the index # of the first position of where the search item was found
print(str1.rfind('s'))      # Returns the last position of where the search item was found
print(str1.rindex('s'))     # Returns the last position of where the search item was found
print()
