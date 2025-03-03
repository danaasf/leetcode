from audioop import reverse
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []

        while matrix:
            # Add first row
            res.extend(matrix.pop(0))
            
            # Add last column
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            # Add last row in reverse order
            if matrix:
                res.extend(matrix.pop()[::-1])
            
            # Add first column in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res

# Explanation:
# Pop the first row → It gets added directly to res.
# Pop the last column → Iterates through remaining rows and removes the last element.
# Pop the last row in reverse → Adds the bottom-most row in reverse order.
# Pop the first column in reverse → Iterates bottom to top and removes the first element.
# Repeat until the matrix is empty.
# This approach correctly follows the spiral order while handling edge cases efficiently


        # res = []
        # res.append(matrix[0])
        # matrix.remove(matrix[0])
        # x = matrix[n-1]
        # res.append(x[::-1])
        # matrix.remove(x)
        # res.append([sub[0] for sub in matrix])
        # res.append([sub[m-1] for sub in matrix])
        
        # print(res)
        # print(matrix)


sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol.spiralOrder(matrix)