'''

Looping in Python : For Loop

'''

print("Script Starting...")

x = 1

print("\n\nLooping from 0..8\n\n")

for each in range(9):
    print("-", each)

print("\n\nLooping from 1..8\n\n")

for each in range(1, 9):
    print("-", each)

print("\n\nLooping from 1..8. Interval 2 \n\n")

for each in range(1, 9, 2):
    print("-", each)


print("\n\nContinue Usage : Will skip the print invocation for 3\n\n")

# Used when we want to jump a certain interation

for each in range(9):
    if(each == 3):
        continue
    print("-", each)

print("\n\nBreak Usage : Will stop the print Invocation post 2\n\n")

# Used when we want to jump a certain interation

for each in range(9):
    if(each == 3):
        break
    print("-", each)

# Looping Used over array

print("\n\nFor Loop in Array\n\n")
array = ["Earth", "Sun", "Mars", "Jupiter", "Saturn"]

for each in array:
    print("Element: ", each)


# Looping Used over Dictionary

print("\n\nFor Loop in Dictionary\n\n")
person = {
    "firstName": "Jonny",
    "lastName":  "Shaw",
    "Age": 21,
    "Gender": "Female",
    "Address": " Bank street, London , UK - 3353433",
    "Bank": ["HDFC", "PayTM"]
}

for key, value in person.items():
    print(key, " : ", value)

# Nested Loop

print("\n\nNested Loop\n\n")

for each in range(9):
    print("###########", each)
    for other in range(each):
        print("#", other)

# TODO: What does range return ?
print("\n\nScript Executed")
