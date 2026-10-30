"""
Problem Link : https://practice.geeksforgeeks.org/problems/deque-implementations/1
Platform     : GFG
Difficulty   : Easy
"""

from collections import deque

class MyDeque:


    def __init__(self):
        self.dq = deque()

    def addFront(self, x):
        self.dq.appendleft(x)

    def addBack(self, x):
        self.dq.append(x)

    def removeFront(self):
        if self.isEmpty():
            return -1
        return self.dq.popleft()

    def removeBack(self):
        if self.isEmpty():
            return -1
        return self.dq.pop()

    def elementAtFront(self):
        if self.isEmpty():
            return -1
        return self.dq[0]

    def elementAtBack(self):
        if self.isEmpty():
            return -1
        return self.dq[-1]

    def isEmpty(self):
        return len(self.dq) == 0

    def size(self):
        return len(self.dq)


