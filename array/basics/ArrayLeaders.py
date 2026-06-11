"""
You are given an array arr of positive integers. 
Your task is to find all the leaders in the array.
An element is considered a leader if it is greater than or equal to all elements to its right.

Examples:
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
"""
class Solution:
    def leaders(self, arr):
        res=[]
        maxR=arr[-1]
        res.append(maxR)
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=maxR:
                maxR=arr[i]
                res.append(arr[i])
        return res[::-1]        
"""
Approach:
The idea is to scan all the elements from right to left in an array and keep track of the maximum till now.
When the maximum changes its value, add it to the result. Finally reverse the result 

Approach	      Time
Brute Force	    O(n²)
Optimal	        O(n)

worst case space: O(n)
"""
