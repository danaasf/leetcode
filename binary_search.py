# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        #print(left,mid,right)
        while (left <= right):
            mid = (right+left)//2 
            if (target>nums[mid]):
                left=mid+1
                #print(left,mid,right)
            elif (target<nums[mid]):
                right= mid-1
            else:
                return mid
            

        return -1
        
sol = Solution()
a= [-1,0,3,5,9,12]
target = 2
print(sol.search(a,target))