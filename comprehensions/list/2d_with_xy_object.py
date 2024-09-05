# -*- coding: utf-8 -*-

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
my_2D_list = [[Point(x, y) for x in range(10)] for y in range(10)]

print(my_2D_list)
