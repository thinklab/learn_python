#!/usr/bin/env python3
from itertools import repeat, islice
import operator


def my_repeat(elem, count=None):
    return MyRepeatPseudoContainer(elem, count)


class MyRepeatPseudoContainer:
    def __init__(self, elem, count):
        self.elem = elem
        self.count = count
        
    def __iter__(self):
        return MyRepeatIterator(self.elem, self.count) 

class MyRepeatIterator:
    def __init__(self, elem, count):
        self.elem = elem
        self.count = count
        
    def __next__(self):
        if self.count == None:
            return self.elem
        else:
            if self.count == 0:
                raise StopIteration()
            self.count -= 1
            return self.elem    
                       

if __name__ == '__main__':
    print(list(islice(repeat(10, ), 20)))
    print(list(islice(my_repeat(10, ), 20)))
    
    print(list(repeat(10, 4)))
    print(list(my_repeat(10, 4)))
    
    
