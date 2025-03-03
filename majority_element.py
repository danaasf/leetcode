# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) space
        # my_dict = {}
        # for a in nums: 
        #     if a in my_dict:
        #         val = my_dict[a]
        #         val +=1
        #         my_dict[a] = val
        #     else:
        #         my_dict[a] = 1

        # for a in my_dict:
        #     if my_dict[a]> len(nums)//2:
        #         return a

        # O(1) space
        nums.sort()
        return nums[len(nums)//2]
        
        return -1 
        