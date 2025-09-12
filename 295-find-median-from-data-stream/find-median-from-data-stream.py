import heapq

class MedianFinder:
    def __init__(self):
        self.low = []   # max heap (store negative values for max behavior)
        self.high = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: push to max heap (low)
        heapq.heappush(self.low, -num)

        # Step 2: balance so every num in low <= every num in high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Step 3: balance sizes (low can have 1 extra element)
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]  # max heap root
        return (-self.low[0] + self.high[0]) / 2.0
