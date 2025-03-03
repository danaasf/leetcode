# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # we need to perform DFS on the matrix 
        # first we want to find the root

        root = word[0]
        roots = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == root:
                    roots.append((i,j))
        
        if roots is None:
            return False
        
        
        def dfs(i,j,k):

            if k == len(word) :
                return True 
                
            if i < 0 or i>= len(board) or j<0 or j>= len(board[0]) or board[i][j]== 0 :
                return False
            
            

            if board[i][j] != word[k] :
                return False
            
            temp = board[i][j]
            board[i][j]= 0
            found = (dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1))

            board[i][j] = temp
            return found 


        for ir,jr in roots:
            if dfs(ir,jr,0):
                return True 
        
        return False


