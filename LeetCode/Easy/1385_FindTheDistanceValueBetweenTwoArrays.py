"""
Problem Link : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num in arr1:
            found = False

            for x in arr2:
                if abs(num - x) <= d:
                    found = True
                    break

            if not found:
                count += 1

        return count
