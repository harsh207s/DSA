class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lowercase_word = set(word.lower())
            if lowercase_word.issubset(row1) or lowercase_word.issubset(row2) or lowercase_word.issubset(row3):
                result.append(word)
        
        return result
