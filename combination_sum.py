# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combinations (candidates,target): 
            if target == 0:
                return [[]]  # Return a list containing an empty combination
            if not candidates or target < 0:
                return []  # No valid combinations

            n = candidates[0]  # First candidate
            if n > target:
                return []  # Skip if the candidate is larger than the target

            # if target < 0 :
            #     return combinations(candidates[1:],target)

            n = candidates[0]
            first =  combinations(candidates,target-n)
            second = combinations(candidates[1:],target)

            first = [[n] + a for a in first]
            

            return first + second 


        return combinations(candidates,target)
         
        




        
        
sol = Solution()
a = [2,3,6,7]
target = 7
print(sol.combinationSum(a,target))



        