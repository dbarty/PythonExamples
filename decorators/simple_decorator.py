# -*- coding: utf-8 -*-
    
def my_decorator(func, before="(", after=")"):
    # Passing the args is important, if the function accepts arguments.
    # Mandatory when decorating methods (needs self)
    def inner(*args, **kwargs): 
        return before + func(*args, **kwargs) + after
    return inner
    
@my_decorator
def greeting(name="World"):
    return f"Hello {name}!"
    
print(greeting())
print(greeting("Daniel"))
