#!/usr/bin/env python3
import itertools
import operator


def get_fib_numbers():
    return MyFib()
class MyFib:
    def __iter__(self):
        return MyFibIter()
class MyFibIter:
    def __init__(self):
        self.prev = 1
        self.next = 1
        self.i = 0
    def __next__(self):
        if self.i < 2:
            self.i+=1
            return 1
        prev = self.next
        next = self.prev + self.next
        self.next = next
        self.prev = prev       
        return next 
        

if __name__ == '__main__':
    c = get_fib_numbers()
    print(list(itertools.islice(get_fib_numbers(), 10, 20)))
    print(list(itertools.islice(get_fib_numbers(), 0, 10)))
    
    
