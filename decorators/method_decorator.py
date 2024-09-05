# -*- coding: utf-8 -*-
    
def my_decorator(func, before="(", after=")"):
    # Passing the args is important, if the function accepts arguments.
    # Mandatory when decorating methods (needs self)
    def inner(*args): 
        return before + func(*args) + after
    return inner
    
class Person:
    def __init__(self, name):
        self.name = name
        
    @my_decorator
    def __str__(self):
        return self.name

person = Person("Daniel")
print(person)
