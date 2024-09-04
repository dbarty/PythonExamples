# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person = Person("Erna", 42)

print(person.name, person.age)
