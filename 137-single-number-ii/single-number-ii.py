from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):  # check each bit
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> i) & 1
            if bit_sum % 3 != 0:
                # Handle negative numbers for the sign bit (31st bit)
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        return result
