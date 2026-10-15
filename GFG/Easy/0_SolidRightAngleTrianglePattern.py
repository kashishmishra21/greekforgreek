"""
Problem Link : https://practice.geeksforgeeks.org/problems/right-angle-triangle-1605685807/1
Platform     : GFG
Difficulty   : Easy
"""

n = int(input())

# code here
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
