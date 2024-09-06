# -*- coding: utf-8 -*-

def class_decorator(cls):
    # Modify or enhance the class
    
    def greeting(self, name="World"):
        print(f"Hello {name}!")
        
    cls.greeting = greeting
    return cls

@class_decorator
class Foo:
    ...
    
foo = Foo()
foo.greeting()
