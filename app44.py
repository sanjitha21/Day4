# Example: create an object from an already defined class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object (instance) of the class
p1 = Person("Alice", 20)

# Use the object
p1.display()
