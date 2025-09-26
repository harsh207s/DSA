from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Precompute the sum of every subarray of size k
        sum_k = [0] * (n - k + 1)
        cur_sum = sum(nums[:k])
        sum_k[0] = cur_sum
        for i in range(1, n - k + 1):
            cur_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = cur_sum

        # Step 2: Compute the best left index for every position
        left = [0] * len(sum_k)
        best = 0
        for i in range(len(sum_k)):
            if sum_k[i] > sum_k[best]:
                best = i
            left[i] = best

        # Step 3: Compute the best right index for every position
        right = [0] * len(sum_k)
        best = len(sum_k) - 1
        for i in range(len(sum_k) - 1, -1, -1):
            if sum_k[i] >= sum_k[best]:  # >= for lexicographically smallest
                best = i
            right[i] = best

        # Step 4: Try all middle intervals
        max_total = 0
        result = [-1, -1, -1]
        for j in range(k, len(sum_k) - k):
            i = left[j - k]
            l = right[j + k]
            total = sum_k[i] + sum_k[j] + sum_k[l]
            if total > max_total:
                max_total = total
                result = [i, j, l]

        return result
