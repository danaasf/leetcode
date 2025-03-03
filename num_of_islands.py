# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


class Solution(object):


    def numIslands(self, grid):
       
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(grid,i,j,dir):
            if j<0 or j>=len(grid[0]) or i<0 or i>=len(grid) or grid[i][j]=='0':
                return 
            grid[i][j]='0'
            for k in range(0,len(dir)): 
                search(grid,i+dir[k][0],j+dir[k][1],dir)

        num_of_islands=0
        dir = [[0,-1],[0,1],[-1,0],[1,0]]
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j]=='1'):
                    num_of_islands+=1
                    search(grid,i,j,dir)
        
        return num_of_islands
                    
sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
num = sol.numIslands(grid)
print(num)



        
        