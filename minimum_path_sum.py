# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = []
        dp = [[float('inf')]*(col+1) for i in range(row+1)]
        dp [row][col-1]= 0
        
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                dp[i][j] = dp[i][j] = min(dp[i+1][j],dp[i][j+1])+ grid[i][j]
        return dp[0][0]

        

            

            

        