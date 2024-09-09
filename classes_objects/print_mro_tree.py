# -*- coding: utf-8 -*-
    
def print_mro_tree(classname, intent=0):
    if type(classname).__name__ == 'str':
        classname = globals()[classname]
    
    print(" " * intent, "+- " if intent > 0 else "",classname.__name__, sep="")
    
    for c in classname.__subclasses__():
        print_mro_tree(c, intent+2)
    

print_mro_tree(ArithmeticError)
