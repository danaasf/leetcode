# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        rotation_point = 0
        
        if not nums:
            return -1 

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
        if target >= nums[rotation_point] and target <= nums[-1]:
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
nums = [4,5,6,7,0,1,2]
target = 0 
print(sol.search(nums,target))