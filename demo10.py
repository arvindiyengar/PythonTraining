'''

DataStructure : List

'''

print("Script Starting...")

array = ["Earth", "Sun", "Mars", "Jupiter", "Saturn"]

print("Printing Entire array : ", array)

# Access Element
print("\n\nAccess Element \n\n")
print("First Element: ", array[0])

# Adding a new Element
print("\n\nAppending \n\n")
array.append("Venus")
print("Updated Array : ", array)

# Copy Array
print("\n\nCopying Array \n\n")
array2 = array.copy()

print("New Array : ", array2)

#  Clearing Array
print("\n\nClearing Array \n\n")
array2.clear()
print(array2)

# Length
print("\n\nLength  \n\n")
print("Length  of the Array: ", len(array))

# Insert at a position
print("\n\nInsert at Position \n\n")
print("Old Array : ", array)
array.insert(1, "Captain-Planet")
print("Updated Array : ", array)

# Pop list
print("\n\nPop Values \n\n")
print("Old Array : ", array)
print("Poped Value : ", array.pop())
print("New Array : ", array)

# Sort the list
print("\n\nSorting \n\n")
print("Old Array : ", array)
array.sort()
print("Sorted Array : ", array)

# Index of Element
print("\n\nIndex Search \n\n")
print("Index of Element Earth , post sorting : ", array.index("Earth"))

print("\n\nScript Executed")
