class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    right = mid - 1  # keep looking left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    left = mid + 1  # keep looking right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
