# -*- coding: utf-8 -*-

def configurable_decorator(before="(", after=")"):
    def decorator(func):
        # Passing the args is important, if the function accepts arguments.
        # Mandatory when decorating methods (needs self)
        def inner(*args, **kwargs): 
            return before + func(*args, **kwargs) + after
        return inner
    return decorator
    
deco1 = configurable_decorator()
deco2 = configurable_decorator(">>", "<<")

@deco1
@deco2
@configurable_decorator(" foo "," bar ")
def greeting(name="World"):
    return f"Hello {name}!"
    
print(greeting())
print(greeting("Daniel"))
