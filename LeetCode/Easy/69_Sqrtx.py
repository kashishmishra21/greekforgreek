"""
Problem Link : https://leetcode.com/problems/sqrtx/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1 :
            return 0
        if x == 2 :
            return x-1
        i = 2
        while i * i <= x:
            i +=1
        return i-1
