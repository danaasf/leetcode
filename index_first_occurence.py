# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n= len(haystack)
        m= len(needle)

        i = 0
        for i in range(n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j+=1

            if j==m: 
                #print(i)
                return i  
            
            i+=1
            #print(i)
            
        return -1

sol= Solution()
haystack = "meetcode" #len=8
needle = "meet" #len=5
#print(haystack,needle)
print(sol.strStr(haystack,needle)) #should return -1



