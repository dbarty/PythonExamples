# -*- coding: utf-8 -*-

class Bike:
    def __init__(self, owner):
        self.owner = owner

class Car:
    def __new__(cls, *args, **kwargs):
        return Bike(*args, **kwargs)  # You want a car and get a Bike!
        
        
bike = Bike("Doerte")  # Calls object::__new__()
car = Car("Manni")     # Calls Car::__new__()

print("Bike:", type(bike).__name__, bike.owner)
print("Car:", type(car).__name__, car.owner)
