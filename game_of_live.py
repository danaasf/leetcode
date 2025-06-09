from typing import List
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

 

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # copy = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))] 
        neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        # no_change = []
        # queue = deque([])
        # queue.append((0,0))
        # dp = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = [board[i][j],0]


        for i in range(len(board)):
            for j in range(len(board[0])):
                a = board[i][j][0]
                for [dx,dy] in neighbors:
                    if not (i+dx<0 or j+dy<0 or i+dx>=len(board) or j+dy>=len(board[0])):
                        a += board[i+dx][j+dy][0]
                        # if (i+dx,j+dy) not in no_change and (i+dx,j+dy) not in queue:
                        #     queue.append((i+dx,j+dy))

                if board[i][j][0] == 1 :
                    if a <= 2:
                        board[i][j][1] = 0
                    elif a<=4 :
                        board[i][j][1] = 1
                    else:
                        board[i][j][1] = 0
                else:
                    if a == 3:
                        board[i][j][1]=1
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j][1]
        
                
            
                    

                    


        