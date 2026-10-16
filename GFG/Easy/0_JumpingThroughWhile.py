"""
Problem Link : https://practice.geeksforgeeks.org/problems/jumping-through-while-python/1
Platform     : GFG
Difficulty   : Easy
"""

def printIncreasingPower(x):
    for i in range(1,x+1):
        sq = i ** 2
        if sq > x:
            break
        print(sq,end=" ")
