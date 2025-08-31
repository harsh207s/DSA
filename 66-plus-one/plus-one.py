class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # iterate from last digit backwards
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # if it's 9, set to 0 and carry over
        
        # if all digits were 9
        return [1] + [0] * n
