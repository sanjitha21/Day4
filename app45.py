# Inheritance in Python
# Inheritance allows a class to reuse the properties and methods of another class.
# The parent class is called the base class or superclass.
# The child class is called the derived class or subclass.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow!"


# Example usage
pet1 = Dog("Buddy")
pet2 = Cat("Milo")

print(pet1.name)       # Buddy
print(pet1.speak())     # Buddy barks: Woof!
print(pet2.name)        # Milo
print(pet2.speak())     # Milo meows: Meow!

# Inheritance helps us avoid repeating code and create specialized classes.
