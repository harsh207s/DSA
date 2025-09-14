from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all integers to strings
        nums_str = list(map(str, nums))

        # Sort using custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Join the sorted strings
        result = ''.join(nums_str)

        # Edge case: if result is all zeros (e.g. ["0", "0"])
        return '0' if result[0] == '0' else result
