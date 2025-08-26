class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):  # No need to check last index
            farthest = max(farthest, i + nums[i])
            
            if i == end:   # Must jump here
                jumps += 1
                end = farthest

        return jumps
