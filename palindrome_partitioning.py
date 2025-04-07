from typing import List
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

class Solution:
    def isPalindrome(self, s:str, l , r):
        while l<r:
            if s[l] != s[r]:
                return False
            l=l+1
            r=r-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []
        def dfs(i):
            if i == len(s):
                res.append(part[:])
                return 
            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res        