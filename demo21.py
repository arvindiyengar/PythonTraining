'''

Classes - Special Methods

'''


class Person:

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

    def __len__(self):
        return 0

    def __str__(self):
        # Type Cast
        return self.name + " is a  " + self.gender + " of age " + str(self.age)

    def __del__(self):
        print("All done")


p = Person("John", 30, "Male")

print("\n\nAccessing Class")

print("length of Person", len(p), "\n\n")
print(p, "\n\n")
print("Script Done")

# TODO: Why does Script Done print before __del__
