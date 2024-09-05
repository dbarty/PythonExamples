# -*- coding: utf-8 -*-

class CustomError(Exception):
    def tooFewCheese():
        return CustomError("Too few cheese!")
    
    def tooMuchCheese():
        return CustomError("Too much cheese!")
    
# Usage

try:
    raise CustomError.tooFewCheese()
except Exception as e:
    print(type(e).__name__, e)
    
try:
    raise CustomError.tooMuchCheese()
except Exception as e:
    print(type(e).__name__, e)
