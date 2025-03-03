# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        res= [1]*(len(nums))

        prefix= 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]

        postfix = 1
        for n in range(len(nums)-1,-1,-1):
            res[n] = res[n]*postfix
            postfix= postfix*nums[n]
        
        return res
        # mul = 1 
        # mul_zero = 1 
        # check = 0
        # count = 0
        # answer = []

        # for a in nums: 
        #     if a==0:
        #         check=1
        #         count+=1
        #         mul*=a
        #     else:
        #         mul*=a
        #         mul_zero*=a

        #     answer.append(0)     

        # if count== len(nums):
        #     return answer  

        # if(count==1):

        #     if check==1: 
        #         for i,a in enumerate(nums):
        #             if a==0:
        #                 answer[i]= mul_zero
        #             else: 
        #                 answer[i]= mul//a
            

        #     else:
        #         for i in range(0,len(nums)):
        #             answer[i]=mul//nums[i]

        # elif count>1:
        #     for i in range(0,len(nums)):
        #             answer[i]=0
        # else: 
        #     for i in range(0,len(nums)):
        #             answer[i]=mul//nums[i]


        # return answer
        

        