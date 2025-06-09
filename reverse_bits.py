# Reverse bits of a given 32 bits unsigned integer.

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

class Solution:
    def reverseBits(self, n: int) -> int:
        x = ""
        
        for i in range(32):
            x += "1" if n & (1<<i) else "0"
        
        #print(x)
        res = 0
        for i,a in enumerate(x[::-1]):
            if a == "0" :
                continue 
            else:
                res+= 2**(i)

        return res

#this is done O(n) space, but there is a more optimal way

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res