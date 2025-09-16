class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n//2, we can complete as many transactions as we want
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

        # DP table: dp[t][d]
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]
