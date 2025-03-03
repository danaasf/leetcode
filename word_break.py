# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.



from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we want to check if there's more than one option, we return false
        # to count the option we use backtracking 
        @lru_cache(maxsize=None)
        def options(cur): 
            if cur == s :
                # we found an option 
                return True

            if not s.startswith(cur):
                return False

            for word in wordDict:
                if not options(cur+word):
                    continue 
                return True 
                #cur.strip(word)
            return False
        
        return options("")
        

            


            
            
            
        
                


             

        