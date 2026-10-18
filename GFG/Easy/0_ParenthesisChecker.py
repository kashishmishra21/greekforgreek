"""
Problem Link : https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        pairs={
            ")":"(",
            "]":"[",
            "}":"{" 
                
        }
        
        for ch in s :
            

            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
                
                    
                
        
