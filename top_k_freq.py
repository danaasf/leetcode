import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_max = []   
        heapq.heapify(heap_max) 
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num] += 1
        
        for (k,v) in freq.items():
            heapq.heappush(heap_max,(-v,k))
        
        return [(heapq.heappop(heap_max)[1]) for i in range(k)]