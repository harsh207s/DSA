class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]  # start with first element as candidate

        while left <= right:
            # If the array is already sorted (no rotation)
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # If mid element is in the left sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res
