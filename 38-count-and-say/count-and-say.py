class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        s = "1"
        for _ in range(n - 1):  # build up to nth term
            i = 0
            next_seq = []
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                next_seq.append(str(count) + s[i])
                i += 1
            s = "".join(next_seq)
        
        return s
