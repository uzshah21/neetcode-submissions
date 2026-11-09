class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = float('inf')
        best_price = 0

        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                best_price = max(best_price, price - cheapest)

        return best_price
        