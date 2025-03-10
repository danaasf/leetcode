# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(0,len(temperatures)):
            res.append(0)
        
        stack = []

        for i in range(0,len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                index = (stack.pop())[1]
                res [index] = i - index
            
            stack.append((temperatures[i],i))

        return res


