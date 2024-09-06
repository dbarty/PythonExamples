# -*- coding: utf-8 -*-

def catch_error(error_handler=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if None != error_handler:
                    error_handler(e)
                else:
                    print("Error occured!", e)
        return inner
    return decorator
                
def error_handler(e):
    print("error_handler(): Error occured!", e)

@catch_error()
def make_error():
    raise Exception("Some random error")
   
@catch_error(error_handler)
def make_error2():
    raise Exception("Some other random error")
    
@catch_error()
def no_error():
    return 42 
   
make_error()
make_error2()
print(no_error())
