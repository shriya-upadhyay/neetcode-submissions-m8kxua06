class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = prices[0]
        max_profit = 0

        for i in range (len(prices)):
            if prices[i] <= local_min:
                local_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - local_min)



        return max_profit


        