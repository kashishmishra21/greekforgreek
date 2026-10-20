"""
Problem Link : https://practice.geeksforgeeks.org/problems/print-square--105330/1
Platform     : GFG
Difficulty   : Basic
"""

class Solution:
    def printHollowSquare(self, n):
        # code here
        for row in range(n):
            for col in range(n):
                if row == 0 or col == 0 or row == (n-1) or col == (n-1):
                    print("*",end=" ")
                else:
                    print(" " , end=" ")
            print()
                    
