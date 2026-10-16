"""
Problem Link : https://leetcode.com/problems/prime-subset-selection-i/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution(object):
    def maxPrimes(self, n, s):
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for j in range(p * p, n + 1, p):
                    is_prime[j] = False
            p += 1

        result = []
        total = 0

        for p in range(2, n + 1):
            if is_prime[p] and total + p <= s:
                result.append(p)
                total += p

        return result


