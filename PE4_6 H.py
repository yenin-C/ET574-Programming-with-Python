#A
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[1])          # Output: 2 (Element at index 1)
print(n[0:10])       # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (Entire list, full slice)
print(n[8], n[-1])   # Output: 9 10 (Element at index 8 and last element using negative indexing)
print(n[3])          # Output: 4 (Element at index 3)
print(n[1:5])        # Output: [2, 3, 4, 5] (Slice from index 1 to 4)
print(n[-5:-1])      # Output: [6, 7, 8, 9] (Slice from index -5 to -2)
print(n[4:8])        # Output: [5, 6, 7, 8] (Slice from index 4 to 7)
#The code shows how to slice and index a list of length n. Elements may be accessed using both positive and negative indices, and the list can be partially extracted via slicing.

#B
print(n[-1], n[-2])   # Output: 10 9 (Last two elements using negative indexing)
print(n[2], n[5])     # Output: 3 6 (Elements at index 2 and 5)
print(n[0], n[3])     # Output: 1 4 (Elements at index 0 and 3)
print(min(n), max(n), len(n), sep='\n')   # Output: 1 \n 10 \n 10 (Minimum, maximum, and length of the list)
print(min(n), max(n), type(n), sep='\t')  # Output: 1 \t 10 \t <class 'list'> (Minimum, maximum, and type of the list)
#This block demonstrates how to access items, even those with negative indices, at certain indices. It also prints the list's length, minimum, and maximum using the functions min(), max(), and len(). The object's kind (list) is printed on the final line.

#C
n[0], n[3] = "apple", "cherry"  # Replacing index 0 with "apple" and index 3 with "cherry"
n.insert(3, "banana")           # Insert "banana" at index 3
n.insert(1, "kiwi")             # Insert "kiwi" at index 1
print(n)                        # Output: ['apple', 'kiwi', 2, 'banana', 'cherry', 5, 6, 7, 8, 9, 10] 
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?")  # Output: Do you like APPLE or 10?
#This block demonstrates replacing elements in a list and inserting new elements at specific positions. The insert() method is used to add items at given indices. Finally, it uses string formatting and .upper() to capitalize and format the string for output.

#D
n.append(-11)       # Adds -11 to the end of the list
n[0], n[10] = n[-1], n[-2]  # Swaps the first element with the last one, and the second-to-last with the second element
print(n)            # Output: Swapped and modified list with -11 at the end
#The append() method adds a new element to the end of the list. Then the first element is swapped with the last element, and the second-to-last element is swapped with the second one.

#E
item1 = n.pop(0)   # Removes and returns the first element
print(f"{item1} is removed.")  # Output: "apple is removed."
item2 = n.pop()    # Removes and returns the last element
print(f"{item2} is removed.")  # Output: "-11 is removed."
print(f"Removed items: {item1} & {item2}")  # Output: "Removed items: apple & -11"
#This block shows how the pop() method works, removing an element from the list and returning it. The first pop removes the element at index 0, and the second pop removes the last element of the list.

#F
n.insert(6, "pear")  # Insert "pear" at index 6
del n[1]             # Deletes the element at index 1
del n[0]             # Deletes the first element
print(n)             # Output: Modified list with deletions
n.remove("pear")     # Removes the first occurrence of "pear"
print('n = ', n)     # Output: Prints the list after removing "pear"
n.clear()            # Clears the entire list
print(f'n = {n}')    # Output: "n = []" (Empty list)
#This block covers list manipulation using insert(), del, remove(), and clear(). It inserts "pear", removes elements by index and by value, and finally clears the entire list, making it empty.

#G 
fruits = ["kiwi", "pear", "orange", "apple", "cherry"]
fruits.sort()        # Sort the list alphabetically
print(fruits)        # Output: ['apple', 'cherry', 'kiwi', 'orange', 'pear']
print(fruits[0], fruits[-1])  # Output: apple pear (First and last element in sorted list)
fruits.sort(reverse=True)     # Sort the list in reverse alphabetical order
print(fruits[0], fruits[-1])  # Output: pear apple (First and last element in reverse-sorted list)
#This part involves sorting a list of fruits alphabetically and printing the first and last element. The list is then sorted in reverse alphabetical order, and the first and last elements are printed again.
