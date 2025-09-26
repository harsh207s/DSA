class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # Define knight moves for each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        # Initialize dp: ways to reach each digit at step 0
        dp = [1] * 10

        for _ in range(1, n):
            next_dp = [0] * 10
            for digit in range(10):
                for nei in moves[digit]:
                    next_dp[digit] = (next_dp[digit] + dp[nei]) % MOD
            dp = next_dp

        return sum(dp) % MOD
