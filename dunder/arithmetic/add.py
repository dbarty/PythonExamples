# -*- coding: utf-8 -*-

class Price:
    def __init__(self, value):
        self.value = int(value)
        
    def __add__(self, other):
        return Price(self.value + other.value)
    
price1 = Price(100)
price2 = Price(200)

price3 = price1 + price2  # '+' calls __add__()

print(price3.value)
