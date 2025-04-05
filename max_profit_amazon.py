
from typing import List

from numpy import sort


class Solution:
  def calculateMaxProfit(self, price: List[int], futurePrice: List[int], principle: int) -> int:
    profit = [0]*len(price)
    res = 0
    
    for i in range(0,len(price)):
      profit[i] = futurePrice[i]-price[i]

    profit.sort()

    
    for i in range(len(price)-1,-1,-1):
      if profit[i] <= 0 :
        continue
      if principle >= price[i]: 
        principle -= price[i]
        res += profit[i]

    return res
      
    
sol = Solution()
sol.calculateMaxProfit( [10, 50, 30, 40, 70], [100, 40, 50, 30, 90], 100)
