# -*- coding: utf-8 -*-

class Price:
    def __init__(self, value, currency = "EUR"):
        self.value = value
        self.currency = currency
    
    def __repr__(self):
        return f"Price({self.value} {self.currency})"
    
    def __lt__(self, other):
        return self.value < other.value
    
p15 = Price(15) 
p05 = Price(5)
p10 = Price(10)
prices = [p15, p05, p10]

print(prices)
prices.sort()
print(prices)

print(p05 < p10)
print(p15 < p10)
