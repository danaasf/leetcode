# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0 , 0,0
        for i in range(len(nums)):
            if (nums[i]==0):
                zero+=1
            elif (nums[i]==1):
                one+=1
            else:
                two+=1

        for i in range(zero):
            nums[i]=0
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,len(nums)):
            nums[i]=2

        return nums


        

        