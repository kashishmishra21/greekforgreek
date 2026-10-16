"""
Problem Link : https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
Platform     : GFG
Difficulty   : Medium
"""

class Solution:
    def subarraySum(self, arr, target):
        # code here
        i = 0 
        total = 0
        for j in range(len(arr)):
            total  += arr[j]
            while i <= j and total > target:
               total -= arr[i]
               i +=1
               
               
            if total == target :
                return [i+1,j+1]
        return [-1]
