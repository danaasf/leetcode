class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper (x,n):
            if n == 0:
                return 1 
            if x == 0 :
                return 0
            
            res = helper(x, n//2)
            res = res*res

            return x*res if (n%2) else res
        

        a = helper(x,abs(n))
        return a if n>=0 else 1/a
        