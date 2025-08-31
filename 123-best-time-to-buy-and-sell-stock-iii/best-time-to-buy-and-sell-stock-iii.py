class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)          # Best after buying first stock
            sell1 = max(sell1, buy1 + price)  # Best after selling first stock
            buy2 = max(buy2, sell1 - price)   # Best after buying second stock
            sell2 = max(sell2, buy2 + price)  # Best after selling second stock
        
        return sell2
