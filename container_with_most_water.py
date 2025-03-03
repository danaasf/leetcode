# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the containe


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start , end = 0 , len(height)-1
        max_water = 0

        while (start < end and end <= len(height)-1 ):
            container = min(height[start],height[end]) * (end-start) 
            print(container)
            if container >= max_water :
                max_water = container 
            

            if (height[end]>height[start]):
                start +=1 
            elif (height[end]<height[start]):
                end -=1
            else:
                start+=1
                end-=1
        

        return max_water 





        