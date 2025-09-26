from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []  # max heap to store fuel from passed stations
        fuel = startFuel
        prev = 0
        refuels = 0
        i = 0
        n = len(stations)

        while fuel < target:
            # Add all reachable stations to the max heap
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(max_heap, -stations[i][1])  # max heap using negative fuel
                i += 1
            
            # If we can't reach further and heap is empty, we’re stuck
            if not max_heap:
                return -1
            
            # Refuel at the station with the most fuel seen so far
            fuel += -heapq.heappop(max_heap)
            refuels += 1

        return refuels
