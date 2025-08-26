class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # 1162261467 = 3^19 (largest power of 3 in 32-bit signed int range)
        return 1162261467 % n == 0
