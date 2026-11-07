"""
Problem Link : https://leetcode.com/problems/process-tasks-using-servers/
Platform     : LeetCode
Difficulty   : Medium
"""

import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        free = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(free, (weight, i))

        ans = []

        for j, task in enumerate(tasks):

            # Release all servers that have completed their tasks
            while busy and busy[0][0] <= j:
                time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no server is free, wait for the earliest one
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] == time:
                    end_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Assign the task to the best available server
            weight, idx = heapq.heappop(free)

            ans.append(idx)

            heapq.heappush(busy, (j + task, weight, idx))

        return ans
