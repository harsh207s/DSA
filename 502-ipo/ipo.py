import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine projects into (capital_required, profit) and sort by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        i = 0
        n = len(projects)
        
        for _ in range(k):
            # Add all affordable projects to max heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Max heap using negative profits
                i += 1
            
            # If no projects are affordable, break
            if not max_heap:
                break
            
            # Take the most profitable project
            w += -heapq.heappop(max_heap)
        
        return w
