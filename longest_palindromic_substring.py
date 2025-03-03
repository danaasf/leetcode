# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_left = 0
        max_right = 0
        max_len = 0
        for i in range(len(s)):        
            left , right = i , i
            length = 0
            while left>= 0 and right<len(s):
                if s[left] == s[right]:
                    length= right - left + 1
                    left -=1
                    right +=1
                else:
                    break 
        
            if (length>max_len):
                max_len = length 
                max_left = left+1 
                max_right = right-1 


            left , right = i , i+1
            length = 0
            while left>= 0 and right<len(s):
                if s[left] == s[right]:
                    length= right - left + 1
                    left -=1
                    right +=1
                else:
                    break 

            if (length>max_len):
                max_len = length 
                max_left = left+1 
                max_right = right-1

        return s[max_left:max_right+1]

sol = Solution()
s = "abb"
print(sol.longestPalindrome(s))