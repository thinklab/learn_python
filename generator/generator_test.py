#!/usr/bin/env python3

def gen_test():
    yield 1
    yield 2
    yield 3
g1 = g2 = gen_test()
#g2 = gen_test()
print(g1)
print(g2)

print(list(g1))
print(list(g1))

print(list(g2))
