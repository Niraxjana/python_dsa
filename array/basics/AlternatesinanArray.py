"""
Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 3 5
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
Take fifth element: 5
"""
class Solution:
    def getAlternates(self, arr):
        result = []
    # Loop from 0 to the end, skipping by 2
        for i in range(0, len(arr), 2):
            result.append(arr[i])
        return result

"""
range(start, stop, step)
start = 0
stop = len(arr)
step = 2
"""
