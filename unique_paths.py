# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.
from functools import lru_cache


class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        # visited = []

        # @lru_cache (None)
        # def aux(i,j):

        #     if (i<0 or i>=m or j<0 or j>=n or ((i,j) in visited)):
        #         return 0

        #     if i == m-1 and j == n-1 :
        #         return 1 
        #     visited.append((i,j))

            
                
        #     result = aux(i + 1, j) + aux(i, j + 1)
        #     visited.remove((i,j))

        #     return result 

        # return aux(0,0)

        
        dp = [[0] * n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 or j == 0:
                    dp[i][j]= 1
                else: 
                    dp[i][j]=0
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]
       






        



        