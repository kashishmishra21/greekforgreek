"""
Problem Link : https://practice.geeksforgeeks.org/problems/slicing-in-string-python/1
Platform     : GFG
Difficulty   : Easy
"""

def joinMiddle(bound, tag):
    """ code here """
    mid = len(bound)//2
    return bound[:mid] + tag + bound[mid:]

