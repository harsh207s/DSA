class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def count_live_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),         (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            return live_neighbors

        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)

                # Rule 1 or 3
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Alive → Dead

                # Rule 4
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Dead → Alive

        # Finalize the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
