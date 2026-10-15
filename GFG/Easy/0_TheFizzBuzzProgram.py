"""
Problem Link : https://practice.geeksforgeeks.org/problems/the-fizzbuzz-program/1
Platform     : GFG
Difficulty   : Easy
"""

n = int(input())

# code here
if n % 3 == 0  and n % 5 != 0:
    print("Fizz")
elif n % 5 == 0  and n % 15 != 0:
    print("Buzz")
elif n % 15 == 0:
    print("FizzBuzz")
else:
    print(n)
