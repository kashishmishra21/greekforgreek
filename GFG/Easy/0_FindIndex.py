"""
Problem Link : https://practice.geeksforgeeks.org/problems/find-index-1614919939--145853/1
Platform     : GFG
Difficulty   : Easy
"""

arr = tuple(map(int, input().split()))
x = int(input())

for i in range(len(arr)):
    if arr[i] == x:
        print(i)
    

########### Write your code below ###############
# Print the index of x in arr

########### Write your code above ###############
