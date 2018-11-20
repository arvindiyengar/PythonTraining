import json

'''

DataStructures : Dictionary

'''

print("Script Starting...")

person = {
    "firstName": "John",
    "lastName":  "Snow",
    "Age": 30,
    "Gender": "Male",
    "Address": "1st Cross Kingpin Road, London , UK - 3333"
}

print("Entire Dictionary : ", person)

# Accessing Attributes
print("\n\nAccessing Attributes\n\n")
print("Accessing First Name : ", person["firstName"])
print("Accessing Last Name : ", person.get("lastName"))

# Changing last Name

print("\n\nEditing Attributes\n\n")
person["lastName"] = "Sharma"
print("Updated dictionary : ", person)

# Accessing all Attributes Keys

print("\n\nAccessing Attributes Keys \n\n")
for each in person:
    print("Attribute Key : ", each)

# Accessing all Attributes Values

print("\n\nAccessing Attributes Values \n\n")
for each in person.values():
    print("Attribute Value : ", each)

# Accessing all Attributes Combined key and value

print("\n\nAccessing Attributes Key and Value \n\n")
for key, value in person.items():
    print(key, " : ", value)

# Check if key present

print("\n\nChecking Attributes Key availability \n\n")

if ("Age" in person.keys()):
    print("Age attribute is present")
else:
    print("Age attribute not found")


# Check for length

print("\n\nLength of Dictionary\n\n")
print("Length of Person Dictionary : ", len(person))

print("\n\nIntroduction to JSON\n\n")

str1 = '{"name": "John Snow", "Age": 30}'
person2 = json.loads(str1)
print("Type of Person2 : ", type(person2))
print("Person2 Dictionary : ", person2)

print("\n\nScript Executed")
