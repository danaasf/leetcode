# Given two strings s and p, return an array of all the start indices of p's 
# anagrams
#  in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hist_p = {}
        res = []
        for c in p : 
            if c in hist_p:
                x = hist_p[c]
                hist_p[c] = x+1
            else:
                hist_p[c] = 1

        window_hist = {}
        for i in range (len(s)):
            window_hist[s[i]]=  window_hist.get(s[i], 0) + 1

            if i>= len(p):
                left_char= s[i-len(p)]
                if window_hist[left_char]==1:
                    window_hist.pop(left_char)
                else:
                    window_hist[left_char] = window_hist.get(left_char) -1 
            
            if window_hist == hist_p :
                res.append(i-len(p)+1)
        
        return res