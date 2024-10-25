class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("Faye", "17", "Nonbinary")
print("This is: " + p1.name + "." + " They are: " + p1.age + "." + " They are: " + p1.gender + ".")