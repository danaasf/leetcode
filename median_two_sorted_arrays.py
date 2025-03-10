from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #we can't merge the lists since the run time complexity is O(log(m+n))
        total = len(nums1)+len(nums2)
        half = total // 2

        if len(nums1)>len(nums2):
            A,B = nums2,nums1
        else:
            A,B = nums1,nums2

        l = 0 
        r = len(A)-1
       
        while (True):
            i = (l + r) // 2
            j = half - i - 2 

            leftA = A[i] if i>=0 else float("-infinity")
            rightA = A[i+1] if (i + 1) < len(A) else float("infinity")
            leftB = B[j] if j>=0 else float("-infinity")
            rightB = B[j+1] if (j + 1) <len(B) else float("infinity")

            if rightA >= leftB and rightB>= leftA :
                if (total % 2) :
                    return min(rightA, rightB)
                else: 
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2
            
            elif rightA <leftB: 
                
                l = i + 1 
                
            else:
                r = i - 1 
                
                


        

        