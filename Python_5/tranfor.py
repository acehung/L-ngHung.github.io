class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        
        self.car_type = "Car"

    def __str__(self):
        return f"{ self.year } {self.brand} {self.model} - Loại xe: {self.car_type}"

class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def __str__(self):
        return f"{ self.year } {self.brand} {self.model} - Loại xe: {self.bike_type}"
my_bike = Bike("Yamaha", "MT-07", 2021, "Motorcycle")
print(my_bike)