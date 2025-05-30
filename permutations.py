from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         #backtracking 
#         res = []
#         if len(nums)==1: 
#             return [nums[:]]

#         for i in range(len(nums)):
#             n=nums.pop(i)
#             perms = self.permute(nums)

#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.insert(i, n)
        
#         return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(nums,current):
            if not nums:
                result.append(current[:])
                return current

            for i in range(len(nums)):
                add = nums[0]
                nums.pop(0)
                current.append(add)
                backtrack(nums,current)
                current.pop()
                #backtrack(nums,current)
                nums.append(add)
        
            return result
        
        return backtrack(nums,[])




            



        