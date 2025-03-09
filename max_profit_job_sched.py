# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

import bisect
from typing import List


class Solution:
    

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))
        res = 0
        cache = {}
        #@lru_cache(maxsize=None)
        def dfs(i):
            if i == len(intervals):
                return 0
            
            if i in cache:
                return cache[i]

            #include 
            res = dfs(i+1)

            #don't include
            j = i + 1
            # while (j < len(intervals)):
            #     if intervals[j][0] >= intervals[i][1]:
            #         break 
            #     j+=1
            j = bisect.bisect(intervals,(intervals[i][1],-1,-1))
            cache[i] = max(res, intervals[i][2]+dfs(j))
            res = cache[i]

            return res 
        
        return dfs(0)

        
