# You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

# You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

# Return an array output where output[j] is the result of query[j].

# Note: The length of an interval is calculated as right_i - left_i + 1.

# Example 1:

# Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]

# Output: [2,2,3,5,1,-1]
import heapq
from typing import List


class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        my_heap= []
        heapq.heapify(my_heap)
        intervals.sort()
        book = []
        for i,q in enumerate(queries):
            book.append((q,i))
        book.sort()

        output= [-1]* len(queries)
        pointer = 0
        for q,idx in book:
            while pointer<len(intervals) and intervals[pointer][0]<= q:
                heapq.heappush(my_heap,(intervals[pointer][1]-intervals[pointer][0]+1,intervals[pointer][1]))
                pointer+=1

            while my_heap and my_heap[0][1] < q:
                heapq.heappop(my_heap)
                
            if my_heap:
                (s,r) = my_heap[0]
                output[idx]= s
        
        return output




            
            



