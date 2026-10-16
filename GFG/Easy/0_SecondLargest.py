"""
Problem Link : https://practice.geeksforgeeks.org/problems/second-largest3735/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution:
    def getSecondLargest(self, arr):
        # code here
        le = len(arr)
        if le <=1:
            return -1
        
        max_arr = max(arr)
        while max_arr in arr:
            arr.remove(max_arr)
        
        if len(arr) == 0:
            return -1
        elif len(arr) == 1:
            return arr[0]
        else:
            max_ar = max(arr)
            return max_ar
        
        
