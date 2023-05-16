#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    
def square_integers(int_list):
   numbers  =  [num ** 2 for num in int_list]
   return numbers
    

def fizzbuzz():
    i = 1
    while i <= 100:
        print(fizzBuzz(i))  
        i=i+1

def fizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i