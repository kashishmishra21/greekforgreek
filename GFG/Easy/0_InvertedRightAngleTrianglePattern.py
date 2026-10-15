"""
Problem Link : https://practice.geeksforgeeks.org/problems/inverted-right-angletriangle-1605691171--104349/1
Platform     : GFG
Difficulty   : Easy
"""

n = int(input())

# code here
for i in range(n,0,-1):
    for j in range(i):
        print("*" , end="")
    print()
