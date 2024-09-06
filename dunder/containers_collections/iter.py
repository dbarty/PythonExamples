# -*- coding: utf-8 -*-

class Group:
    def __init__(self):
        self.members = []
        
    def __iter__(self):
        return iter(self.members)
    
    def add(self, person):
        if type(person).__name__ == "Person":
            self.members.append(person)
            
            
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

group = Group()
group.add(Person("Daniel"))
group.add(Person("Helga"))

# Group::__iter__() is called and returns the iterator (the list 'self.members') for group
# list_iterator::__next__() is called with each loop
for member in group:
    print(member)
