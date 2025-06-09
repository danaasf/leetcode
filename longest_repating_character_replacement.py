# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


from collections import defaultdict
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l , r = 0 , 0
        res = 0
        hashmap = collections.defaultdict(int)

        while l<=r and r<len(s):
            hashmap[s[r]] += 1
            length = r - l + 1
            common = 0
            for key,value in hashmap.items():
                if value>common:
                    common = value 
            if (length - common) <= k:
                res = length 
                r+=1
            else :
                hashmap[s[l]] -=1 
                l+=1
                r+=1

        
        return res 



        


        