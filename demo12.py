'''

DataStructures : Sets

'''

print("Script Starting...")


set1 = {"Earth", "Sun", "Mars", "Jupiter", "Saturn"}

set2 = {"Earth", "Uranus"}

# Change an element

print("Entire Set : ", set1)

# set1[1] = "New Planet" # Throws an error

# Adding a new value

print("\n\nAdding new value\n\n")
print("Old set :", set1)
set1.add("Venus")
print("Updated Set : ", set1)

# copy the set

print("\n\Copying new Set\n\n")
set3 = set1.copy()
print("Copied Set", set3)

# Union of 2 sets

print("\n\nUnion Operation\n\n")
print("Set1 : ", set1)
print("Set2 : ", set2)
print("Union Set : ", set1.union(set2))

# Union of 2 sets

print("\n\nIntersection Operation\n\n")
print("Set1 : ", set1)
print("Set2 : ", set2)
print("Union Set : ", set1.intersection(set2))

print("\n\nScript Executed")
