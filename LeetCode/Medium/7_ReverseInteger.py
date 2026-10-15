"""
Problem Link : https://leetcode.com/problems/reverse-integer/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            n = x % 10 
            rev = (rev * 10) + n
            x = x // 10
        return rev * sign
        
