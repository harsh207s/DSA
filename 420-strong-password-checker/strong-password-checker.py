class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing = 3 - (has_lower + has_upper + has_digit)

        replace = 0
        one = two = 0

        i = 0
        while i < n:
            j = i
            while i < n and password[i] == password[j]:
                i += 1
            length = i - j
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        use = min(delete, one)
        replace -= use
        delete -= use

        use = min(delete, two * 2)
        replace -= use // 2
        delete -= use

        use = delete // 3
        replace -= use

        return (n - 20) + max(missing, replace)