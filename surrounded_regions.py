# 130. Surrounded Regions

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = []
        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>= len(board[0]) or (i,j) in visited or board[i][j]!='O':
                return False
            # if (board[i-1][j]== 'X' and board[i][j-1]=='X') or (board[i-1][j]== 'X' and board[i][j+1]=='X') or (board[i][j-1]== 'X' and board[i+1][j]=='X') or (board[i+1][j]== 'X' and board[i][j+1]=='X'):
            #     return 1 
            board[i][j] = 'T'

            dfs(i-1,j)  
            dfs(i+1,j)  
            dfs(i,j-1)  
            dfs(i,j+1)
                
            # counter = dfs(i-1,j)+ dfs(i+1,j)+ dfs(i,j-1)+ dfs(i,j+1) 
            # if counter == 4:
    
       
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == 'O' and  (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1):
                    dfs(i,j) 
                else:
                    continue 

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    


        