"""
Problem Link : https://practice.geeksforgeeks.org/problems/stacks-operations/1
Platform     : GFG
Difficulty   : Basic
"""

class myStack:
    # Define your stack
    def __init__(self):
        self.arr = []

    def push(self, x):
       self.arr.append(x)
        

    def pop(self):
        if len(self.arr) == 0:
            return -1
        else:
            self.arr.pop()
        

    def peek(self):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]
        
    def getSize(self):
        
        return len(self.arr)
        
    def isEmpty(self):
        return len(self.arr) == 0
            
        
