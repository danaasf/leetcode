from typing import List
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        #dp[i] = the maximum amount of money we have so much after stealing houses until house at the index n 
        res = 0

        for n in range(0,len(nums)):
            if n == 0: 
                dp[n] = nums[n]
                continue
                
            
            if n == 1:
                dp[n] = max(dp[0],nums[1])
                continue
                
            
            dp[n] = max(dp[n-1],dp[n-2]+nums[n])
            
        


        return dp[len(nums)-1]

        

        