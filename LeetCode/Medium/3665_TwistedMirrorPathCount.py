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

                ways = dp[i][j]

                # Move right
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        dp[i][j + 1] = (dp[i][j + 1] + ways) % MOD
                    elif i + 1 < m:
                        r, c = i + 1, j + 1
                        while r < m and c < n and grid[r][c] == 1:
                            r += 1
                        if r < m and c < n:
                            dp[r][c] = (dp[r][c] + ways) % MOD

                # Move down
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        dp[i + 1][j] = (dp[i + 1][j] + ways) % MOD
                    elif j + 1 < n:
                        r, c = i + 1, j + 1
                        while r < m and c < n and grid[r][c] == 1:
                            c += 1
                        if r < m and c < n:
                            dp[r][c] = (dp[r][c] + ways) % MOD

        return dp[m - 1][n - 1]
