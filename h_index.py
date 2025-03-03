# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        print(citations)
        for idx, citation in enumerate(citations):

            # find the first index where citation is smaller than or equal to array index            
            if idx >= citation:
                return idx
        # We want to find out the amount of articles h that have been cited at least h times each. 
        # Attempt : sort of a histogram, in which the amount of articles in i - are the ones cited i+ times

        #Brute force approach
        # hist= []
        # m = max(citations)
        
        # for n in range(0,m+1):
        #     hist.append(0)


        # for i in range(0,len(citations)):
        #     j = 0
        #     while j <= citations[i]:
        #         hist[j]+=1
        #         j+=1
      
        # #print(hist[len(hist)-1]>=len(hist)-1)
        # for b in range(len(hist)-1, -1, -1):

        #     if hist[b] >= b:
        #         return b
        
        # return -1

        


    




sol = Solution()
a = [3,0,6,1,5]
sol.hIndex(a)

