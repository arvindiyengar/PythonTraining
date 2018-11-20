'''

Classes - Inheritance

'''


class Person:
    count = 0
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
        Person.count += 1

    def __str__(self):
        # Type Cast
        return self.name + " is a  " + self.gender + " of age " + str(self.age)

    @staticmethod
    def hello():
        print("Hello Person, This is from Static Method")

    def sayHi(self):
        print(self.name + " is of the type Person")

    def printSalary(self):
        print(self.name + " earns " + str(self.salary))


class Teacher (Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, gender)
        self.salary = 1000

    def sayHi(self):
        print(self.name + " is of the type Teacher")


class Dancer (Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.salary = 5000

    def sayHi(self):
        print(self.name + " is of the type Dancer")


p = Person("John", 30, "Male")
p1 = Teacher("Jane", 31, "Female")
p2 = Dancer("Joe", 33, "Male")
p1.printSalary()
p2.printSalary()

p1.sayHi()
p2.sayHi()
p.sayHi()

Person.hello()
print("Total Count : ", Person.count)
