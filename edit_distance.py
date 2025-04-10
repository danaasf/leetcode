# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [( [float("inf")] * (len(word2)+1)) for i in range(len(word1)+1)]
        dp[len(word1)][len(word2)]= 0
        for i in range(0,len(word1)):
            dp[i][len(word2)]= len(word1)-i
        for i in range(0,len(word2)):
            dp[len(word1)][i]= len(word2)-i
        
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] != word2[j]:
                    dp[i][j]= 1 + min(dp[i+1][j+1],dp[i][j+1],dp[i+1][j])
                else:
                    dp[i][j] = dp[i+1][j+1]
        
        print(dp)
        
        return dp[0][0]
        
        