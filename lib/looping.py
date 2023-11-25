#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0,-1):
        print(i)
        if i == 1 : print("Happy New Year!")

def square_integers(int_list):
    int_list = [i**2 for i in int_list]
    return int_list

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
