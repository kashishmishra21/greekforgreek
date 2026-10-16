"""
Problem Link : https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution:
    def missingNum(self, arr):
        # code her
        n = len(arr) + 1
        expected_sum = n * (n + 1) // 2
        actual_Sum = sum(arr)
        return expected_sum - actual_Sum
