# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"[Person: {self}]"
    
people = [Person("Helga", 42), Person("Stefan", 23)]

print(people)  # Calls Person::__repr__() in list view
print(people[0])  # Calls Person::__str__() in single view
