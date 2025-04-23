import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap,(grid[0][0],0,0))
        visited.add((0,0))
        while (heap):
            cell = heapq.heappop(heap)
            value , i , j = cell[0] , cell[1] , cell[2]
            if i == len(grid)-1 and j==len(grid[0])-1:
                return value
            
            for d in directions:
                if i+d[0]<0 or i+d[0]>=len(grid) or j+d[1]<0 or j+d[1]>=len(grid[0]) or (i+d[0],j+d[1]) in visited:
                    continue 
                visited.add((i+d[0],j+d[1]))
                heapq.heappush(heap,(max(grid[i+d[0]][j+d[1]],value),i+d[0],j+d[1]))
        
        
                


