"""
Problem Link : https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1
Platform     : GFG
Difficulty   : Basic
"""

n = int(input())

# code here
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num +=1
    print()
    
