class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Helper to convert "a+bi" to (a, b)
        def parse(num: str):
            real, imag = num[:-1].split("+")
            return int(real), int(imag)

        a, b = parse(num1)
        c, d = parse(num2)

        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real = a * c - b * d
        imag = a * d + b * c

        return f"{real}+{imag}i"
