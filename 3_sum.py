# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums)==0:
                return [nums]
            else:
                return []

        res = set()

        for i in range(0,len(nums)):
            left = i+1
            target = -nums[i] 
            cur = []        
            hashmap = {}

            while left < len(nums):
                hashmap[left] = nums[left] 
                if target - nums[left] in hashmap.values():
                    cur = [nums[i],target- nums[left], nums[left]]
                    res.add(cur)
            
                left+=1
        





        return list(res)



                
