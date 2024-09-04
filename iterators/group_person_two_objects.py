# -*- coding: utf-8 -*-

class MemberIterator:
    def __init__(self, members):
        self.members = members
        
    def __next__(self):
        try:
            return self.members.pop(0)
        except:
            raise StopIteration()

class Group:
    def __init__(self):
        self.members = []
        
    def __add__(self, person):
        if type(person).__name__ == "Person":
            self.members.append(person)
            
    def __iter__(self):
        return MemberIterator(self.members)
            
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

group = Group()
group + Person("Daniel")  # Calls Group::__add__()
group + Person("Helga")

# Group::__iter__() is called and returns the MemberIterator for group
# MemberIterator::__next__() is called with each loop
for member in group:
    print(member)    
