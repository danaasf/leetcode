# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        rotten = deque()
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        #bfs

        while rotten and fresh>0: 
            minutes+=1 
            for _ in range(len(rotten)):
                i , j= rotten.popleft()
                for di,dj in [(0,-1),(0,1),(-1,0),(1,0)]:
                    ii = i + di
                    jj= j+ dj
                    #check in bound
                    if ii<0 or ii>=len(grid) or jj<0 or jj>=len(grid[0]):
                        continue 
                    
                    if grid[ii][jj]==0 or grid[ii][jj]==2:
                        continue 
                    
                        
                    grid[ii][jj]=2
                    fresh -=1
                    rotten.append((ii,jj))

        
        return minutes if fresh==0 else -1

        