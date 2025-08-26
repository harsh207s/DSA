class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # अगर input खाली है तो return []
            return []
        
        # Digit-to-letter mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []

        def backtrack(index, path):
            # अगर path की length digits की length के बराबर है तो एक valid combination मिला
            if index == len(digits):
                res.append("".join(path))
                return
            
            # current digit से letters निकालना
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return res
