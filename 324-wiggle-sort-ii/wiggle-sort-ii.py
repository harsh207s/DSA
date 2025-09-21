from typing import List
import random

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        def nth_element(nums, n):
            def select(left, right, n_smallest):
                if left == right:
                    return nums[left]

                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)

                if n_smallest == pivot_index:
                    return nums[n_smallest]
                elif n_smallest < pivot_index:
                    return select(left, pivot_index - 1, n_smallest)
                else:
                    return select(pivot_index + 1, right, n_smallest)

            def partition(left, right, pivot_index):
                pivot = nums[pivot_index]
                nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
                store_index = left

                for i in range(left, right):
                    if nums[i] < pivot:
                        nums[store_index], nums[i] = nums[i], nums[store_index]
                        store_index += 1

                nums[right], nums[store_index] = nums[store_index], nums[right]
                return store_index

            return select(0, len(nums) - 1, n)

        # Step 1: Find median
        median = nth_element(nums[:], len(nums) // 2)

        # Step 2: 3-way partition using virtual index
        def index(i):
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[index(i)] > median:
                nums[index(left)], nums[index(i)] = nums[index(i)], nums[index(left)]
                left += 1
                i += 1
            elif nums[index(i)] < median:
                nums[index(right)], nums[index(i)] = nums[index(i)], nums[index(right)]
                right -= 1
            else:
                i += 1
