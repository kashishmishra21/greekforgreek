"""
Problem Link : https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
       
        maxi = max(nums)
        count = 0
        for i in range(len(nums)):
            while nums[i] != maxi:
                nums[i] +=1
                count +=1
        return count

        
