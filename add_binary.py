# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        
        if (len(a)> len(b)):
            for i in range (0, len(a)-len(b)):
                b= '0'+b
        else:
            for i in range (0, len(b)-len(a)):
                a= '0' +a
        
        
        res = [0]*len(a)
        a = list(a)
        b = list(b)
        carry = 0
        

        for i in range(len(a)-1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            current = total % 2
            carry = total // 2
            res[i] = str(current)


        if carry==1:
            res.insert(0,'1')


        s = ''.join(res) 
        return s 


        
            
            
        