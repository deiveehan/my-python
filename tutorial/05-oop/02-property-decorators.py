class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be positive")

# Using the class
p = Person("Alice", 30)
print(p.age)  # Accessing the age (getter)
p.age = 35   # Setting a new age (setter)
