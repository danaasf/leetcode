# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

from typing import List

    
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

       
        def fill(image: List[List[int]],color,original,i,j):
            if (i<0 or j<0 or i>=len(image) or j>=len(image[i]) or image[i][j]== color or image[i][j]!=original):
                return
            else:
                image[i][j]=color
                fill(image,color,original,i,j+1)
                fill(image,color,original,i,j-1)
                fill(image,color,original,i+1,j)
                fill(image,color,original,i-1,j) 
          
               
               


        original= image[sr][sc]
        #image[sr][sc]=color
        fill(image,color,original,sr,sc)
        
 
       

        return image
        
        


    



sol = Solution()
a= [[0,0,0],[0,0,0]]
sr= 0
sc = 0
color=0
print(sol.floodFill(a,sr,sc,color))