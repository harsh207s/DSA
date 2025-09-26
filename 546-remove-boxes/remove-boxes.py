class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            
            # Merge same-colored boxes at the start
            while l < r and boxes[l] == boxes[l+1]:
                l += 1
                k += 1
            
            # Option 1: remove boxes[l] now
            res = (k+1) * (k+1) + dp(l+1, r, 0)
            
            # Option 2: try to merge boxes[l] with later same color
            for m in range(l+1, r+1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l+1, m-1, 0) + dp(m, r, k+1))
            
            return res
        
        return dp(0, len(boxes)-1, 0)
