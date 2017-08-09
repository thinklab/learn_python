#!/usr/bin/env python3

from itertools import *

class MyFibNum:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return MyFibIterator(self.n)

class MyFibIterator:
    def __init__(self, n):
        self.n = n
    def __next__():
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        return []
        
if __name__ == '__main__':
    print(list(MyFibNum(10)))
    
