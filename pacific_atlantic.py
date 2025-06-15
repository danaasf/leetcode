# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        neighbors = [[-1,0],[1,0],[0,1],[0,-1]]
        pacific = set()
        atlantic = set()

        def dfs(i,j,visit,prev):
            if (i,j) in visit or (i<0 or j<0 or i>=len(heights) or j>=len(heights[0])) or heights[i][j]<prev:
                return  
            visit.add((i,j))
            for dx,dy in neighbors:
                dfs(i+dx,j+dy,visit,heights[i][j])


        for c in range(len(heights[0])):
            dfs(0,c,pacific, heights[0][c])
            dfs(len(heights)-1,c,atlantic,heights[len(heights)-1][c])
            

        for r in range(len(heights)):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,len(heights[0])-1,atlantic,heights[r][len(heights[0])-1])
            
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append((i,j))

        return res



            
