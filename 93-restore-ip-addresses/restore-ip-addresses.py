class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, parts):
            # If we already have 4 parts and used all chars -> valid IP
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]

                # Invalid if leading zero (unless it's "0")
                if len(segment) > 1 and segment[0] == "0":
                    continue

                # Invalid if > 255
                if int(segment) > 255:
                    continue

                # Choose this segment
                backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return res
