from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket = num // width

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[old // width]

        return False
