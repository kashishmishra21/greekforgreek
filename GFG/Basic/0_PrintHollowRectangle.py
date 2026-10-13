"""
Problem Link : https://practice.geeksforgeeks.org/problems/hollow-rectangle-or-square/1
Platform     : GFG
Difficulty   : Basic
"""

n = int(input())
m = int(input())

# code here
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or i == n -1 or j == m - 1:
            print("*" , end="")
        else:
            print(" ", end="")
    print()
