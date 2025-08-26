class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x *= sign  # make x positive

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # check for overflow before multiplying
            if rev > (INT_MAX - digit) // 10:
                return 0
            rev = rev * 10 + digit

        return sign * rev
