from typing import List
import heapq
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        result = []
        heap = [(0, float('inf'))]
        prev_height = 0

        for x, neg_h, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))

            curr_height = -heap[0][0]
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height

        return result
