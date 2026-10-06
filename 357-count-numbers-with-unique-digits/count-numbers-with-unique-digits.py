class Solution:
    def countNumbersWithUniqueDigits(self, n):
        # Handle the special case when n=0
        if n == 0:
            return 1
        
        total = 1  # counting zero as a valid number
        for length in range(1, n + 1):
            count_for_length = 9  # first digit can't be zero (except for length=1)
            available_digits = 9  # digits 1-9 for the first digit (excluding zero)
            for i in range(length - 1):
                count_for_length *= (available_digits - i)
            total += count_for_length
        return total
