class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert nums to a set, which removes duplicates
        # If the length of the set is smaller than nums, duplicates exist
        return len(nums) != len(set(nums))
