# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        return self.name == other.name and self.age == other.age
        
    
person1 = Person("Erna", 42)
person2 = Person("Erna", 42)

print(id(person1), id(person2))  # Different objects, despite same content
print(person1 == person2)  # Calls __eq__()
