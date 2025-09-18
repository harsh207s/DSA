from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        # Extract all trees with height > 1 and sort by height
        trees = sorted((h, i, j) 
                       for i, row in enumerate(forest)
                       for j, h in enumerate(row) if h > 1)

        def bfs(sx, sy, tx, ty):
            if sx == tx and sy == ty:
                return 0
            R, C = len(forest), len(forest[0])
            visited = [[False] * C for _ in range(R)]
            queue = deque([(sx, sy, 0)])
            visited[sx][sy] = True

            while queue:
                x, y, steps = queue.popleft()
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and forest[nx][ny] != 0:
                        if nx == tx and ny == ty:
                            return steps + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny, steps + 1))
            return -1

        total_steps = 0
        cx, cy = 0, 0  # starting point

        for _, tx, ty in trees:
            steps = bfs(cx, cy, tx, ty)
            if steps == -1:
                return -1
            total_steps += steps
            cx, cy = tx, ty
        
        return total_steps
