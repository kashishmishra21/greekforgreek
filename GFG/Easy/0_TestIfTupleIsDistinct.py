"""
Problem Link : https://practice.geeksforgeeks.org/problems/test-if-tuple-is-distinct/1
Platform     : GFG
Difficulty   : Easy
"""

arr = tuple(map(int, input().split()))

# code here
sets = set(arr)

if len(arr) != len(sets):
    print("False")
else:
    print("True")
