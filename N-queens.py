from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() #r+c
        negDiag = set() #r-c
        grid = [ ["."] * n for i in range(n)]
        res = []

        def backtrack(r): 

            if r==n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue 
                
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                grid[r][c]= "Q"
                backtrack(r+1)
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                grid[r][c] = "."
        
        backtrack(0)
        return res

            
        






        