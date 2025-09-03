class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        # Calculate bucket size and count
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Distribute numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # Scan through buckets to find maximum gap
        max_gap = 0
        prev_max = min_val
        for bmin, bmax in buckets:
            if bmin == float('inf'):
                continue
            max_gap = max(max_gap, bmin - prev_max)
            prev_max = bmax

        return max_gap
