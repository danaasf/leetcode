# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        nums = ""
        res = 0
        i = 0
        negative = False
         
        while i < len(s) and s[i] == ' '  :
            i += 1
            # Handle signs
        if i < len(s)  and s[i] == '-':
            negative = True
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
            # Handle digits
        
        while i < len(s) and s[i].isnumeric():
            nums += s[i]
            i += 1
        
            
          # Exit loop if it's neither space, sign, nor numeric    
        digits = 10** (len(nums)-1)
        for num in nums:
            res+= int(num)*digits
            digits = digits // 10

        if res >= 2**31:
            if negative:
                res = 2**31
            else:
                res = 2**31 -1
        
        if negative: 
            return res*(-1)
         
        return res
            
                
            
            
        