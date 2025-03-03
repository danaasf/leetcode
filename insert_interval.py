# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            #check if not overlapping with the interval, then we could just add it to the res, and all intervals that are after 
            if(newInterval[1] < intervals[i][0]): 
                res.append(newInterval)
                return res+ intervals[i:]
            elif (newInterval[0] > intervals[i][1]):
                res.append(intervals[i])
            else: #overlapping intervals, we have to merge with the current interval 
                newInterval= [ min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
                #we don't add it since it might be overlapping with coming intervals

        res.append(newInterval)

        
        return res 




        



sol = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print( sol.insert(intervals,newInterval))