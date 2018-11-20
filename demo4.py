'''

Type Casting / String Manipulations

'''
print("Script Started ...")

# Type Casting : Convertion of one var type to another

# String to Int

x = "12"

print("Old type: ", type(x), x)

new_x = int(x)

print("New type: ", type(new_x), new_x)


# Int to Str

x = 12

print("Old type: ", type(x), x)

new_x = str(x)

print("New type: ", type(new_x), new_x)


# Float to int

x = 12.10

print("Old type: ", type(x), x)

new_x = int(x)

print("New type: ", type(new_x), new_x)

''' 

    String Manipulations

    1. Concat
    2. Count
    3. Find
    3. Index
    4. Substring

'''

str1 = "John"
str2 = "Snow"

# Concat

str3 = str1 + str2
print("Concat Value of str1 and str2", str3)

# Count

print("Count for l :", str3.count('l'))
print("Count for o : ", str3.count('o'))

# Find

print("Index of h: ", str3.find("h"))
print("Index of a: ", str3.find("a"))  # -1 if not found , if yes then index

# Index
print("Index of Snow: ", str3.index("Snow"))

# Substring

print("Substring : ", str3[0:3])
print("Script Executed")
