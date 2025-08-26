class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, step = 0, -1

        for ch in s:
            rows[cur_row] += ch
            # change direction at top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                step = -step
            cur_row += step

        return "".join(rows)
