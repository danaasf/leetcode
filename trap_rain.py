from typing import List

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        max_left , max_right = height[l] , height[r]
        rain = 0
        while (l < r):
            if max_left < max_right:
                l+=1
                rain+= max(max_left-height[l],0)
                max_left = max(max_left, height[l])
                
            else:
                r-=1
                rain+= max(max_right-height[r],0)
                max_right = max(max_right,height[r])
                
        
        return rain

        