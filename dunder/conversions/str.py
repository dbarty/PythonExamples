# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name
    
person = Person("Erna", 42)

print(person)  # Calls __str__()
