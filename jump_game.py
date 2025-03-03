# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=0 
        index = 0 
        
        for j in range (len(nums)):

            while i  < len(nums)-1 : 
                #print(i)
                index = i
                i = i + nums[i]

            if index == len(nums)-1:
                return True
            
            else : 
                j+=1 
                i=j

        return False 


       
sol = Solution()
a = [2 ,3 , 1, 1 ,4]     
for i in range(0,len(a)-1):
    print(a[i])  
sol.canJump(a)

