# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        @lru_cache(maxsize=None)

        def options(current_sum,i ): 
            if current_sum == (nums_sum // 2) :
                # we found an option 
                return True

            if current_sum > (nums_sum //2)  or i>= len(nums):
                return False

            #for num in nums:
                #cur.append(num)
            return ((options(current_sum+nums[i],i+1) or options(current_sum,i+1)))
                #return False
                #cur.pop()
            #return False

       
        return options(0,0)