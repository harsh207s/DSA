class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # remove leading/trailing spaces
        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True
        
        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True
            elif char in ['+', '-']:
                # sign must appear only at start or right after 'e'/'E'
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                # only one dot allowed, and not after 'e'
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in ['e', 'E']:
                # only one 'e' allowed, must follow a number
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False  # must ensure digits after e
            else:
                return False
        
        return num_seen and num_after_e
