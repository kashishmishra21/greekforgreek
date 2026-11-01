"""
Problem Link : https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Platform     : LeetCode
Difficulty   : Medium
"""


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


