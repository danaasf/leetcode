# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[]

        def backtrack(i, path):
            if i >= len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)

        backtrack(0,[])
        return res
    

# sol = Solution()
# nums = [1,2,3]
# print(sol.subsets(nums))

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))




        