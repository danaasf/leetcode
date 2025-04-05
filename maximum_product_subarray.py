from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        maximum , minimum = 1 , 1
        for num in nums:
            if num == 0 :
                maximum , minimum = 1 ,1 
                continue
            print(num,maximum,minimum)
            maximum,minimum= max(num*maximum, num*minimum, num),min(num*maximum, num*minimum, num)

            res = max(res,maximum)
            #print(minimum,maximum)

        return res
        # self.max_product = float("-inf")
        # @lru_cache (maxsize=None)
        # def backtrack(i,current): 
        #     if i == len(nums):
        #         self.max_product = max(self.max_product, current) 
        #         return

        #     self.max_product = max(self.max_product, current) 
        #     backtrack(i+1, nums[i])
        #     backtrack(i+1, current*nums[i])
            


        # backtrack(1,nums[0])
    
        # return self.max_product

        