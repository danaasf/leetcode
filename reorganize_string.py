# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 
import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        heap = [[-val,key] for key,val in count.items()]
        heapq.heapify(heap)

        prev = None
        res = ""

        while heap or prev:

            if prev and not heap:
                return ""

            maxfrq, char = heapq.heappop(heap)
            res+= char
            maxfrq +=1

            if prev:
                heapq.heappush(heap,prev)
                prev = None

            if maxfrq < 0 :
                prev = [maxfrq,char] 


        return res
        