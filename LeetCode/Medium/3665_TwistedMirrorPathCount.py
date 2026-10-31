"""
Problem Link : https://leetcode.com/problems/twisted-mirror-path-count/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                # Move right
                if j + 1 < n:
                    r, c = i, j + 1

                    while r < m and c < n and grid[r][c] == 1:
                        r += 1

                    if r < m and c < n:
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

                # Move down
                if i + 1 < m:
                    r, c = i + 1, j

                    while r < m and c < n and grid[r][c] == 1:
                        c += 1

                    if r < m and c < n:
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]


