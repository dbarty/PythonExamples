# -*- coding: utf-8 -*-

class Price:
    def __init__(self, value):
        self.value = int(value)
        
    def __int__(self):
        return self.value
    
price1 = Price(100)
price2 = Price(200)

print(int(price1) + int(price2))  # int() calls __int__()
