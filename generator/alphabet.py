# -*- coding: utf-8 -*-

def alphabet_generator(upper=False):
    codes = (65, 91) if upper else (97, 123)
    
    for code in range(*codes):
        yield chr(code)
 
for char in alphabet_generator():
    print(char, end=" ")

for char in alphabet_generator(True):
    print(char, end=" ")
