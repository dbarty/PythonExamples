# -*- coding: utf-8 -*-

class CallMeLikeAFunction:
    def __init__(self, whatever):
        self.whatever = whatever
        
    def __call__(self):
        print("CallMeLikeAFunction::__call__()")
        print(f"You can access 'whatever': {self.whatever}")
        
        
cmlaf = CallMeLikeAFunction("Just testing")

cmlaf()  # Calls __call__()
