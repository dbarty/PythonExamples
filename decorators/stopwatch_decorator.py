# -*- coding: utf-8 -*-

import time

def stopwatch_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.5} seconds to execute")
        return result
    return wrapper

@stopwatch_decorator
def heavy_load(duration=2):
    time.sleep(duration)  # sleep for x seconds
    
heavy_load()
heavy_load(4)
