from typing import List
import math

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A regular number in mathematics is defined as one which evenly divides some power of 60. 
# Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

# These numbers have had many applications, from helping ancient Babylonians keep time to tuning 
# instruments according to the diatonic scale.

# Given an integer N, write a program that returns, in order, the first N regular numbers.


def get_regular_numbers(n: int) ->  List:
    """
    Returns a list of regular numbers in the range of 1 to n (inclusive),
    A regular number is an integer with prime divisors 2, 3, and 5 only.
    """
    regs = []
    for i in range(1,n+1):
        if regular_number(i):
            regs.append(i)
    return(regs)

def regular_number(i: int) -> bool:
    if primeFactors(i) == [2, 3, 5.0]:
        return True
    return False

def primeFactors(n): 
    "A function to print all prime factors of a given number n "
    
    lst = []
    while n % 2 == 0: 
        lst.append(2) 
        n = n / 2
        
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            lst.append(i) 
            n = n / i 
              
    if n > 2: 
        lst.append(n) 
    
    # a bad way of removing dups from this quick implementation
    return(list(set(lst)))

if __name__ == "__main__":
    lst = get_regular_numbers(3600)
    print(f"All regular numbers between 1 and 3600:")
    print(lst)