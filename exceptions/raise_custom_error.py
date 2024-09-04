# -*- coding: utf-8 -*-

class NotAPersonError(TypeError):
    ...

class Group:
    def __init__(self):
        self.members = []
        
    def add(self, person):
        if not type(person).__name__ == "Person":
            raise NotAPersonError(f"Unable to add this type: {type(person)}")
        
        self.members.append(person)
            
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name          
          
group = Group()

for item in [Person("Stefan"), "WrongType"]:
    try:
        group.add(item)
        print(f"{item} added!")
    except NotAPersonError as e:
        print("Error: ", e)
