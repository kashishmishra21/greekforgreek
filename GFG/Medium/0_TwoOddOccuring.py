"""
Problem Link : https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1
Platform     : GFG
Difficulty   : Medium
"""

class Solution:
    def twoOddNum(self, arr):
        xor = 0

        for num in arr:
            xor ^= num

        rightmost_set_bit = xor & -xor

        num1 = 0
        num2 = 0

        for num in arr:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return sorted([num1, num2], reverse=True)
