'''

DataStructures : Nested

'''

print("Script Starting...")

person = {
    "firstName": "John",
    "lastName":  "Snow",
    "Age": 30,
    "Gender": "Male",
    "Address": "1st Cross Kingpin Road, London , UK - 3333",
    "Bank": ["SBI", "CitiBank", "IDBI", "HDFC", "PayTM"]
}


print("\n\nAccessing Name of person : ",
      person["firstName"] + " " + person["lastName"])
# This is concat of 2 strings

persons = [
    {
        "firstName": "John",
        "lastName":  "Snow",
        "Age": 30,
        "Gender": "Male",
        "Address": "1st Cross Kingpin Road, London , UK - 3333",
        "Bank": ["SBI", "CitiBank", "IDBI", "HDFC", "PayTM"]
    },
    {
        "firstName": "Jonny",
        "lastName":  "Shaw",
        "Age": 21,
        "Gender": "Female",
        "Address": " Bank street, London , UK - 3353433",
        "Bank": ["HDFC", "PayTM"]
    },
    {
        "firstName": "Sam",
        "lastName":  "Sharma",
        "Age": 33,
        "Gender": "Male",
        "Address": "Baker Street, London , UK - 123241",
        "Bank": ["HDFC", "PayTM", "CitiBank"]
    }

]
print("\n\nAccessing 2 Person's Name : ",
      persons[1]["firstName"] + " " + persons[1]["lastName"])

print("\n\nScript Executed")
