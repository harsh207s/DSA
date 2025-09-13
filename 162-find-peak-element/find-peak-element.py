class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than next → peak is on the left side (including mid)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                # Else peak is on the right side
                left = mid + 1
        
        # left == right → peak found
        return left
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than next → peak is on the left side (including mid)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                # Else peak is on the right side
                left = mid + 1
        
        # left == right → peak found
        return left
