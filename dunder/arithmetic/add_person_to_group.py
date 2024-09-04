# -*- coding: utf-8 -*-

class Group:
    def __init__(self):
        self.members = []
        
    def __add__(self, person):
        if type(person).__name__ == "Person":
            self.members.append(person)
            
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

group = Group()
group + Person("Daniel")  # Calls Group::__add__()
group + Person("Helga")

for member in group.members:
    print(member)  
