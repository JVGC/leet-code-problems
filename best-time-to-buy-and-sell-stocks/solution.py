from typing import List


class Solution(object):
    def maxProfitN2(self, prices: List[int]) -> int:
      """
      :type prices: List[int]
      :rtype: int
      """
      max_profit = 0
      for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
          if (prices[j] - prices[i]) > max_profit:
            max_profit = prices[j] - prices[i]

      return max_profit if max_profit > 0 else 0

    def maxProfit(self, prices: List[int]) -> int:
      """
      :type prices: List[int]
      :rtype: int
      """

      max_profit = 0
      least_value_so_far = prices[0]

      for current_value in prices[1:]:
        if (current_value - least_value_so_far) > max_profit:
          max_profit = current_value - least_value_so_far
        elif current_value < least_value_so_far:
          least_value_so_far = current_value
      return max_profit

solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))