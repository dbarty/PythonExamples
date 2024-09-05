# -*- coding: utf-8 -*-

class MyDecorator:
    def __init__(self, before="(", after=")"):
        self.before = before
        self.after = after
        
    def __call__(self, func):
        def inner(*args, **kwargs):
            return f"{self.before}{func(*args, **kwargs)}{self.after}"
        return inner
        
my_decorator = MyDecorator(">>>", "<<<") 
my_decorator2 = MyDecorator("---", "---") 
       
@my_decorator
@my_decorator2
def greeting(name="World"):
    return f"Hello {name}!"

print(greeting())
print(greeting("Daniel"))
print(greeting(name="Helga"))
