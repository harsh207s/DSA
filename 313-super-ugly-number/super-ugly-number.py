class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n                   
        k = len(primes)
        idx = [0] * k                   
        val = list(primes)               

        for i in range(1, n):
            next_ugly = min(val)
            ugly[i] = next_ugly

            for j in range(k):
                
                if val[j] == next_ugly:
                    idx[j] += 1
                    val[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]
