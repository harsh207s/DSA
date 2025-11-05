class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 to both ends to handle boundaries
        nums = [1] + nums + [1]
        n = len(nums)
        
        # DP table: dp[l][r] = max coins from bursting balloons in (l, r)
        dp = [[0] * n for _ in range(n)]
        
        # length of interval
        for length in range(2, n):  
            for left in range(0, n - length):
                right = left + length
                # try bursting k as last balloon in (left, right)
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        
        return dp[0][n - 1]
