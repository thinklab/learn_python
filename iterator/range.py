#!/usr/bin/env python3
import itertools
import operator


def my_range(n):
    return MyPseudoRangeCon(n) 

class MyPseudoRangeCon:
    def __init__(self, n): 
        self.n = n
    def __iter__(self):
        return MyPseudoRangeIter(self.n)
class MyPseudoRangeIter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __next__(self):
        if self.i == self.n:
            raise StopIteration()
        ret = self.i
        self.i += 1
        return ret
        
        
r = range(10)
mr = my_range(10)

print(list(r))
print(list(r))
print(list(mr))
print(list(mr))
