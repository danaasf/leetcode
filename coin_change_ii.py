# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

# You may assume that you have an unlimited number of each coin and that each value in coins is unique


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make amount 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount + 1)
#         dp[0] = 1
#         for i in range(len(coins) - 1, -1, -1):
#             for a in range(1, amount + 1):
#                 dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
#         return dp[amount]

#O(n)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         coins.sort()
#         dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
#         for i in range(n + 1):
#             dp[i][0] = 1
        
#         for i in range(n - 1, -1, -1):
#             for a in range(amount + 1):
#                 if a >= coins[i]:
#                     dp[i][a] = dp[i + 1][a]  
#                     dp[i][a] += dp[i][a - coins[i]]  

#         return dp[0][amount]

#O(mn)