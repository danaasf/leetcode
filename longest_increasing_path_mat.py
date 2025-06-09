# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(i,j,current):
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]<=current: 
                return 0 
    
            if (i,j) in cache:
                length = cache[(i,j)]
            else: 
                length = max(dfs(i+1,j,matrix[i][j]),dfs(i-1,j,matrix[i][j]),dfs(i,j+1,matrix[i][j]),dfs(i,j-1,matrix[i][j])) + 1
                cache[(i,j)]=length

            return length


      
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    res = max(res,dfs(i,j,-1))
                

        return res



        