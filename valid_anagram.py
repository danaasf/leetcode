# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d= {}
        if(len(t)!=len(s)):
            return False
            
        for a in s:
            if a in d:
                count = d.get(a)
                count +=1
                d[a]= count
            else:
                d.update({a: 1})
    
        for a in t:
            if a not in d:
                return False
            else: 
                count = d.get(a)
                count -=1
                d[a]= count 
        

        for a in d:
            if d.get(a)>0:
                return False

        return True






sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
