from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        
        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:  #stack[-1] is the top element 
                index, height = stack.pop()
                res = max(res, height* (i-index))
                start = index #we can extend backwards 

            stack.append((start,h))

        for i,h in stack:
            res = max(res, h*(len(heights)-i))
        
        return res