class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # clamp to 32-bit signed int max

        # get the sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        # subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return sign * result
