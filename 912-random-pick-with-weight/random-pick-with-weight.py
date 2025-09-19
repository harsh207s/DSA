import random
import bisect
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        r = random.randint(1, self.total)
        # find the leftmost index where prefix[i] >= r
        return bisect.bisect_left(self.prefix, r)
