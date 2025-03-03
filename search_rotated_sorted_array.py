# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # my idea is: first we want to find where the pivot is, so we check left,right,mid,
        # that take O(n) time complexity 
        # afterwards, we peform Binary Search on the two subarray [0,pivot] and [pivot+1,n-1]
 


        left = 0
        right = len(nums)-1
        while (left<right): 
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            if nums[mid] < nums[right]: 
                right = mid 
        pivot = left
        
        left1 = 0 
        left2= pivot
        right1= pivot-1
        right2= len(nums)-1

        if target>=nums[left1] and target<=nums[right1]:
            while(left1<=right1):
                mid1= (left1+right1) // 2
                if target<nums[mid1]:
                    right1 = mid1-1
                elif target> nums[mid1]:
                    left1 = mid1+1
                else: 
                    return mid1
        
        #no return meaning we still haven't found the target, we do Binary Search on the other sub array
        if target>=nums[left2] and target<=nums[right2]:
            while(left2<=right2):
                mid2= (left2+right2) // 2
                if target<nums[mid2]:
                    right2 = mid2-1
                elif target> nums[mid2]:
                    left2 = mid2+1
                else: 
                    return mid2
        
        return -1
                

        



sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 0 
print(sol.search(nums,target))