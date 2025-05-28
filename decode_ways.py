class Solution:
#     You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'

# "2" -> 'B'

# ...

# "25" -> 'Y'

# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.
    
    def numDecodings(self, s: str) -> int:
        my_set = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18",
        "19","20","21","22","23","24","25","26"}

        if s[0] == "0" :
            return 0 

        dp = [0] * len(s)
        dp [0] = 1

        if len(s) >= 2: 
            first = s[0]+s[1]
            if (first in my_set) and s[1] in my_set:
                dp[1] = dp[0] + 1
                
            elif (first in my_set) and not (s[1] in my_set):
                dp[1] = dp[0]

            elif not (first in my_set) and (s[1] in my_set):
                dp[1] = dp[0]
        
        

            for i in range(2,len(s)):
                current = s[i-1] + s[i]
                if current in my_set and s[i] in my_set: 
                    dp[i] = dp[i-1] + dp[i-2]
                elif current in my_set and not s[i] in my_set : 
                    dp[i] = dp[i-2]
                elif current not in my_set and s[i] in my_set:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = 0
            
            return dp[len(s)-1]
        
        else:
            return dp[0]



