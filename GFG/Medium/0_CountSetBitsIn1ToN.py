"""
Problem Link : https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
Platform     : GFG
Difficulty   : Medium
"""

class Solution:
    def countSetBits(self, n):
        count = 0

        while n > 0:
            x = n.bit_length() - 1
            p = 1 << x

            count += x * (p >> 1)
            count += n - p + 1

            n -= p

        return count
