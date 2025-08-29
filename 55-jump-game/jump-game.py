class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0   # farthest index we can reach
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                # If we are stuck before this index
                return False
            max_reach = max(max_reach, i + jump)
            
            if max_reach >= len(nums) - 1:
                return True
        
        return True
