# -*- coding: utf-8 -*-

def my_multi(x):
    def my_inner(y):
        return x * y
    return my_inner
        
my_list = [i for i in range(10)]
multi5 = my_multi(5)
multi10 = my_multi(10)

print("my_list", my_list)
print("my_list map(multi5)", list(map(multi5, my_list)))
print("my_list map(multi10)", list(map(multi10, my_list)))
