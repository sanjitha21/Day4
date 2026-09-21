# Inheritance
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
pet1 = Dog("Buddy")
pet2 = Cat("Milo")

print(pet1.name)      
print(pet1.speak())     
print(pet2.name)       
print(pet2.speak())   
