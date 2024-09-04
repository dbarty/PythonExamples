# -*- coding: utf-8 -*-

class MyService:
    def __enter__(self):
        print("MySevice::__enter__()")
        
    def __exit__(self, exc_type, exc, traceback):
        print("MySevice::__exit__()", exc_type, exc, traceback)
        
with MyService():
    print("Do some stuff...")
