class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, minPrice = 0, 100
        for price in prices:
            minPrice = min(minPrice, price);
            result = max(result, price - minPrice)
        return result
        