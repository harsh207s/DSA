class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):  # iterate from 0 to 2^n - 1
            result.append(i ^ (i >> 1))
        return result
