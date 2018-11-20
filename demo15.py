'''

Condition in Python : If / Else

'''

print("Script Starting...")

x = 3
y = 5

print("\n\nChecking if X is greater than 10\n\n")
if (x > 10):
    print("X is greater than 10")
else:
    print("X is smaller than 10")

print("\n\nChecking if X is greater than 10 or x is greater than 2 \n\n")

if (x > 10):
    print("X is greater than 10")
elif (x > 2):
    print("X is greater than 2")
else:
    print("X is smaller than 2")

print("\n\nChecking if X is greater than 2 And y is greater than 3 \n\n")

if (x > 2 and y > 3):
    print("X is greater than 2 and Y is greater than 3")
else:
    print("X is smaller than 2 and Y is smaller than 3")

print("\n\nOne Line If - Else \n\n")

print("X is greater than 2") if x > 2 else print("X is smaller than 2")


print("\n\nScript Executed")
