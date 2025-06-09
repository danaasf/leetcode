# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window



from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque([])
        for i in range(k):
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append((nums[i],i))
        
        output.append(q[0][0])
        r = k 
        while r<len(nums):
            while q and q[-1][0] <nums[r]:
                q.pop()
            q.append((nums[r],r))
            if q[0][1]< r-k+1:
                q.popleft()
            output.append(q[0][0])
            r+=1
        return output




        