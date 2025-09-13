class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the first element
        res = nums[0]
        
        # Track current max and min products
        cur_max, cur_min = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            
            # If negative, swap because multiplying by negative flips max/min
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            
            # Update current max and min
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            # Update result
            res = max(res, cur_max)
        
        return res
