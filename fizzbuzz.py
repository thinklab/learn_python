#!/usr/bin/env python3
"""Напишите программу, которая выводит на экран числа от 1 до   100. При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
"""

for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
        continue
    if i%3==0: 
        print("Fizz")
        continue
    if i%5==0:
        print("Buzz")
        continue
    print(i)e
