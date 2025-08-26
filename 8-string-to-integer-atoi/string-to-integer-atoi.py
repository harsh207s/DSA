class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i, n = 0, len(s)
        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. Handle sign
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
