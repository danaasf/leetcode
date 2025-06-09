# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.


from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        r , c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        def count_mines(r,c):
            count = 0 
            for dr,dc in neighbors:
                if not (r+dr<0 or r+dr>=len(board) or c+dc<0 or c+dc>= len(board[0])):
                    if board[r+dr][c+dc] == 'M':
                        count+=1
            
            return count
        
        queue = deque([(r,c)])

        while queue:
            r,c = queue.popleft()
            if board[r][c] != 'E':
                continue
            count = count_mines(r,c)
            if count == 0 :
                board[r][c]= 'B'
                for dr,dc in neighbors:
                    if not (r+dr<0 or r+dr>=len(board) or c+dc<0 or c+dc>= len(board[0])):
                        queue.append((r+dr,c+dc))
            else:
                board[r][c] = str(count)

        return board

