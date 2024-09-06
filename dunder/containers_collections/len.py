# -*- coding: utf-8 -*-

class Group:
    def __init__(self):
        self.members = []
        
    def __len__(self):
        return len(self.members)
    
    def add(self, person):
        if type(person).__name__ == "Person":
            self.members.append(person)
            
class Person:
    def __init__(self, name):
        self.name = name


group = Group()
group.add(Person("Daniel"))
group.add(Person("Helga"))

print("Number members:", len(group))  # Calls Group::__len__()
