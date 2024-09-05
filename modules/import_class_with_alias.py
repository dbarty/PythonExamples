# -*- coding: utf-8 -*-

from mymodule import Person as BasePerson

class Person(BasePerson):
    def __init__(self, name, age, job="*unemployed*"):
        super().__init__(name, age)
        self.job = job
        
    def __str__(self):
        return f"{super().__str__()}, {self.job}"
    
person1 = Person("Bobby", 23)
person2 = Person("Helga", 42, "Data Analyst")

print(person1)
print(person2) 
