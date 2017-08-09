#!/usr/bin/env python3
from itertools import islice

def my_cycle(seq, n=None):
    mlist = list(seq)
    if n==None:
        while True:
            for i in range(len(mlist)):
                yield mlist[i]
    else:
        for i in range(n):
            for j in range(len(mlist)):
                yield mlist[j]
                
                
print(list(islice(my_cycle([10, 2, 4]), 10)))

print(list(my_cycle([10, 2, 4], 3)))
    
