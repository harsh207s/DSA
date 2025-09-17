class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)  # Add last bit of n to res
            n >>= 1                    # Shift n right by 1
        return res
