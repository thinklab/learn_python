#!/usr/bin/env python3

def my_range(n):
    for i in range(n):
        yield i
       
def my_range2(n):
    i = 0
    while i<n:
        yield i
        i += 1
        
    
print(list(my_range(100)))

r = range(10)
mr = my_range2(10)

print(list(r))
print(list(r))
print(list(mr))
print(list(mr))
