'''

Classes

'''


class Person:
    alive = True

    '''

    Possible Attributes for a Person:

    1. Name
    2. Age
    3. Gender

    '''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = 0

    def greet(self):
        print("Hello ", self.name)

    def greetByTime(self, time="Morning"):
        print("Hello", self.name, " . ", time)


print("Accessing Static Variable", Person.alive)
p = Person("John", 30, "Male")

print("\n\nAccessing Functions \n\n")
p.greet()
p.greetByTime()
p.greetByTime("Goodnight")

print("\n\nAccessing Variables \n\n")
print(p.name, p.age, p.gender)
