import random
from typing import List

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.reset()

    def flip(self) -> List[int]:
        # pick a random available position
        rand_idx = random.randint(0, self.total - 1)
        
        # get the real index (if swapped before, use the mapped one)
        real_idx = self.map.get(rand_idx, rand_idx)
        
        # move the last available index into rand_idx's place
        self.total -= 1
        self.map[rand_idx] = self.map.get(self.total, self.total)
        
        return [real_idx // self.n, real_idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map = {}
