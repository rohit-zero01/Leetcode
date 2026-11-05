from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        queue = deque()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        # Step 1: Find all rotten and fresh oranges
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 2:
                    queue.append((i, j, 0))

                elif grid[i][j] == 1:
                    fresh += 1

        # Step 2: Four possible directions
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        minutes = 0

        # Step 3: BFS
        while queue:

            i, j, time = queue.popleft()

            minutes = max(minutes, time)

            for row_change, col_change in directions:

                new_row = i + row_change
                new_col = j + col_change

                # Check boundaries
                if 0 <= new_row < rows and 0 <= new_col < cols:

                    # Check if the orange is fresh
                    if grid[new_row][new_col] == 1:

                        # Make it rotten
                        grid[new_row][new_col] = 2
                        fresh -= 1

                        # Add it to the queue
                        queue.append((new_row, new_col, time + 1))

        # Step 4: Final answer
        if fresh > 0:
            return -1

        return minutes