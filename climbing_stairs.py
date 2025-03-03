class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<=2):
            return n
        res = [None]*(n+1)

        return self.helper(n,res)

    def helper (self,n ,res): 
        if(n<=2):
            return n

        if(res[n]):
            return res[n]

        res[n] = self.helper(n-1,res) + self.helper(n-2,res)
            
        return res[n]