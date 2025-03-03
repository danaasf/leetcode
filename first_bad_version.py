# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 # The isBadVersion API is already defined for you.

bad = 5 
class Solution:
    def firstBadVersion(self, n: int) -> int:  
        left = 1
        right = n

        if(left == right):
            return left
    
        while (left<right):
            mid = (right+left)//2
            if (isBadVersion(mid)):
                right = mid
            else:
                
                left= mid + 1

              

        return left


def isBadVersion(version: int) -> bool:
    if (version==bad):
        return True
    else:
        return False

sol= Solution()
a = 6 
sol.firstBadVersion(a)
