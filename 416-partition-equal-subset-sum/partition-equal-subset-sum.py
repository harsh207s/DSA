class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, can't split equally
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[j] means: can we form sum 'j' using some numbers
        dp = [False] * (target + 1)
        dp[0] = True  # sum 0 is always possible (take no elements)
        
        for num in nums:
            # Traverse backwards to avoid reusing the same number
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
