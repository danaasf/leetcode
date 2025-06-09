# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp [len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] :
                    dp[i]= max(dp[i],1+dp[j])                    
                
        return max(dp)
        