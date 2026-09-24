class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        a = prices[0]
        p = 0
        for i in prices:
            if i < a:
                a = i
            elif i-a > p:
                p = i-a
        return p
