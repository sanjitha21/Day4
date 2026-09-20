# Class concept in Python
# A class is a blueprint for creating objects.
# It defines attributes (data) and methods (functions) that the objects will have.

class Car:
    # __init__ is a special method called when an object is created.
    def __init__(self, brand, model, year):
        self.brand = brand   # instance attribute
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."

    def info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"


# Creating objects (instances) of the class
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.info())
print(car1.start_engine())
print(car2.info())

# Explanation:
# - Car is a class.
# - car1 and car2 are objects created from the Car class.
# - Each object has its own attribute values.
# - Methods are actions that objects can perform.
