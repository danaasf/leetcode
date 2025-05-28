

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        rotation_point = 0
        if (nums[r]<nums[l]) :

            while l<r:
                m = (l+r) // 2
                if(nums[m]>nums[r]):
                    l = m+1
                else:
                    r = m
            
            rotation_point = l
        else:
            rotation_point = 0


        left, right = 0 , len(nums)-1
        if target >= nums[rotation_point] and target <= nums[len(nums)-1]:
            left , right = rotation_point , len(nums)-1
        
        else:
            left , right = 0 , rotation_point-1


        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
                    
        return -1 


        
        
sol = Solution()
print(sol.search([3,5,6,0,1,2],4))


