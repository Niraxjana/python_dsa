"""
You are given a sorted array arr[] containing positive integers.
Your task is to remove all duplicate elements from this array such that each element appears only once.
Return an array containing these distinct elements in the same order as they appeared.
"""
class Solution:
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return []

        res = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                res.append(arr[i])

        return res


