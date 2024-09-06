# -*- coding: utf-8 -*-

class Group:
    def __init__(self):
        self.members = []
        
    def __contains__(self, other):
        return other in self.members
    
    def add(self, person):
        if type(person).__name__ == "Person":
            self.members.append(person)
            
class Person:
    def __init__(self, name):
        self.name = name

group = Group()

p1 = Person("Daniel")
group.add(p1)

p2 = Person("Helga")
group.add(p2)

p3 = Person("Thomas")
# We do not add p3!
#group.add(p3)

print(f"Is {p1.name} in group?", p1 in group)  # Calls Group::__contains__()
print(f"Is {p2.name} in group?", p2 in group)
print(f"Is {p3.name} in group?", p3 in group)
