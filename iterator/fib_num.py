#!/usr/bin/env python3
import itertools
import operator

def n_fib_nums3(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib_list = [1, 1]
    for i in map(lambda x,y:(x, y, x+y), fib_list[-2], fib_list[-1]):
        fib_list.append(i)
    return 

def n_fib_nums(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib_list = [1, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-2] + fib_list[-1]) 
    return fib_list

def n_fib_nums2(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib_list = [1, 1]
    prev = 1
    next = 1
    for i in range(n-2):
        prev_prev = prev
        prev = next
        next = prev_prev + next 
        fib_list.append(next) 
    return fib_list    


   
if __name__ == '__main__':
    print(list(n_fib_nums3(10)))
    print(list(n_fib_nums2(10)))
