# -*- coding: utf-8 -*-

class CurrencyError(ValueError):
    ...
    
class NotAPriceError(AttributeError):
    ...
    
class Price:
    def __init__(self, value, currency = "EUR"):
        self.value = float(value)
        self.currency = currency
    
    # conversion
    def __str__(self):
        return f"Price({self.value} {self.currency})"
    
    def __repr__(self):
        return f"Price({self})"
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    # 
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value  
    
    def __ge__(self, other):
        return self.value >= other.value
    
    # arithmetic operators
    def __add__(self, other):
        self.__raiseErrorIfNotMatch(other)
        return Price(self.value + other.value)
    
    def __sub__(self, other):
        self.__raiseErrorIfNotMatch(other)
        return Price(self.value - other.value)
    
    def __mul__(self, factor):
        return Price(self.value * factor)
    
    def __truediv__(self, divider):
        return Price(self.value / divider)
 
    def __floordiv__(self, divider):
        return Price(self.value // divider)
    
    # helper method
    def __raiseErrorIfNotMatch(self, other):
        if type(self) != type(other):
            raise NotAPriceError("The given argument is not a type of Price!")
            
        if self.currency != other.currency:
            raise CurrencyError(f"Currency {self.currency} does not match {other.currency}!")
        
    
### Usage:
    
# Calls Price::__add__()
print(Price(15) + Price(35))    
print(int(Price(15) + Price(35)))    
print(float(Price(15) + Price(35)))   

# Calls Price::__sub__()
print(Price(55) - Price(35))    
print(int(Price(55) - Price(35)))    
print(float(Price(55) - Price(35))) 

print(Price(55) * 2)    # Calls Price::__mul__()
print(Price(199) / 2)   # Calls Price::__truediv__()
print(Price(199) // 2)  # Calls Price::__floordiv__()

# Trigger Errors
price1 = Price(100)
price2 = Price(50, "USD")

try:
    price1 + "Hallo Welt"
except Exception as e:
    print(type(e).__name__, e)
    
try:
    price1 + price2
except Exception as e:
    print(type(e).__name__, e)
