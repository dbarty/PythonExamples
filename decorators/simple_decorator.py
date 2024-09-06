# -*- coding: utf-8 -*-
    
def simple_decorator(func):
    # Passing the args is important, if the function accepts arguments.
    # Mandatory when decorating methods (needs self)
    def inner(*args, **kwargs): 
        return "(" + func(*args, **kwargs) + ")"
    return inner
    
@simple_decorator
def greeting(name="World"):
    return f"Hello {name}!"
    
print(greeting())
print(greeting("Daniel"))
