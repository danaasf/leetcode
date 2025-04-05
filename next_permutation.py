from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        if len(nums)==2 :
            nums.reverse()

        elif nums == sorted(nums, reverse=True):
            nums.sort()

        else:
            i = len(nums)-2
            while (i>0 and nums[i]>=nums[i+1]):
                i-=1
            j = i+1
            smallest_larger = max(nums[i+1:])
            smallest_larger_index = 0


            while (j<len(nums)):
                if nums[j]>nums[i] and nums[j]<=smallest_larger:
                    smallest_larger = nums[j]
                    smallest_larger_index = j
                j+=1
                
            temp = nums[i]
            nums[i]= nums[smallest_larger_index]
            nums[smallest_larger_index]= temp
            nums[i+1:]= sorted(nums[i+1:])


                

            



            

                    
                        
                                




                    



                


        

        

        