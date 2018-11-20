'''

Functions - Param

'''

print("Script Starting...")

# a and b are params here


def add(a, b):
    print("Adding 2 numbers ", a, b)
    return a+b

# One function does the job of adding . Clean code .


print("\n\nSimple Function Call\n\n")
print(add(3, 4))
print(add(31231, 1234))
print(add(989, 1563))


# Pass by Value / Referene
print("\n\nPass by Value\n\n")


def sample(num):
    print("Inside Num function")
    num += 10
    print("Inside Num Value", num)


num = 200
print("Before calling sample , outside : ", num)
sample(num)
print("After calling sample , outside : ", num)

print("\n\nPass by Reference\n\n")


def sampleDict(person):
    print("Inside sampleDict function")
    person["Age"] += 10
    print("Inside Persomn Value", person)


person = {
    "name": "John",
    "Age": 30
}
print("Before calling sampleDict , outside : ", person)
sampleDict(person)
print("After calling sampleDict , outside : ", person)


print("\n\nPass by Reference\n\n")


def sampleArray(planets):
    print("Inside sampleArray function")
    planets.append("Earth")
    print("Inside Persomn Value", planets)


planets = ["Sun", "Jupiter", "Mars", "Venus"]
print("Before calling sampleArray , outside : ", planets)
sampleArray(planets)
print("After calling sampleArray , outside : ", planets)


print("\n\nDefault Param Value\n\n")


def addDefault(num1, num2=20):
    print("Inside addDefault")
    return num1 + num2


x = 20
print("Without overriding -  ", addDefault(20, 30))  # output 50
print("Using default - ", addDefault(20))    # output 40

print("\n\nMultiple param\n\n")


def addMultiple(num1, *numbers):
    print("Inside addMultiple")
    sum = 0
    sum += num1
    for each in numbers:
        sum += each
    print("Sum of all the Param Passed: ", sum)


print("5 Values passed")
addMultiple(10, 20, 30, 40, 50)
print("\n\n3 Values passed")
addMultiple(10, 20, 30)

print("\n\nScript Executed")
