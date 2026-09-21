# Class 
class Car:
   
    def __init__(self, brand, model, year):
        self.brand = brand   # instance attribute
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."

    def info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.info())
print(car1.start_engine())
print(car2.info())

