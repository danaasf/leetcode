from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        res= mat 
        queue =  deque([])
        for i in range(0,len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 0 : 
                    queue.append([i,j])
                else:
                    mat[i][j]= -1
        
        while (queue): 
            [r,c] = queue.popleft()
            for dr,dc in directions:
                
                if  r+dr<0 or c+dc<0 or r+dr>= len(mat) or c+dc>=len(mat[0]) or mat[r+dr][c+dc]!= -1:
                    continue
                else: 
                    mat[r+dr][c+dc]= mat[r][c]+1
                    queue.append([r+dr,c+dc])
            

        return mat

        


