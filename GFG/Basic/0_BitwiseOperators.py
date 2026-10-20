"""
Problem Link : https://practice.geeksforgeeks.org/problems/bitwise-operators-1597314674--135255/1
Platform     : GFG
Difficulty   : Basic
"""

a = int(input())
b = int(input())
c = int(input())

# code here
d = a ^ a
e = c ^ b
f = a & b
g = ~e
print(d, e, f, g)
