# -*- coding: utf-8 -*-

class InfiniteNumbers:
    def __init__(self):
        self.number = 0
        
    def __next__(self):
        self.number += 1
        return self.number
    

inf = InfiniteNumbers()

for _ in range(10):
    print("Next number:", next(inf))  # Calls InfiniteNumbers::__next__()
