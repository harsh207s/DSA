import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to index in ascending order

        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            left, right = l, r
            while left <= right:
                while nums[left] < pivot: left += 1
                while nums[right] > pivot: right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left + 1, right - 1
            
            if k <= right: return quickselect(l, right)
            if k >= left: return quickselect(left, r)
            return nums[k]

        return quickselect(0, len(nums) - 1)
