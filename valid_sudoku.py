from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for row in board:
            seen = set()
            for num in row: 
                if num == "." :
                    continue    
                if num in seen: 
                     return False
                seen.add(num) 
        
        for col in range(9):
            seen = set()
            for row in range(9): 
                if board[row][col]==".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for l in range(0,3):
            for k in range(0,3):
                seen = set()
                for i in range(0,3):
                    for j in range(0,3):
                        if board[k*3 + i][l* 3 + j]==".":
                            continue
                        if board[k*3 + i][l* 3 + j] in seen:
                            return False
                        seen.add(board[k*3 + i][l* 3 + j])
        
        return True

        

        
