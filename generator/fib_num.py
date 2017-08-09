#!/usr/bin/env python3
from itertools import islice

def fib_gen():
    prev = 1
    next = 1
    while True:
        yield prev
        prev_prev=prev
        prev = next
        next += prev_prev
        
def fib_gen2():
    yield 1 
    yield 1
    prev = 1
    next = 1
    while True:
        next_old = next
        next = prev + next
        prev = next_old
        yield next

print(list(islice(fib_gen(), 10)))
print(list(islice(fib_gen2(), 10)))
