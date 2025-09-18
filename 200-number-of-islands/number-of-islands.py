from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    # BFS to mark all connected land
                    q = deque([(i, j)])
                    grid[i][j] = '0'  # mark visited
                    while q:
                        r, c = q.popleft()
                        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr, nc))
        return islands
