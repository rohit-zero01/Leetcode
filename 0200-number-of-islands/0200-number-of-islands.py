# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0
        
        # def bfs(r, c):
        #     queue = deque([(r, c)])
        #     visited.add((r, c))
            
        #     while queue:
        #         curr_r, curr_c = queue.popleft()
        #         # Check all 4 directions
        #         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #             nr = curr_r + dr
        #             nc = curr_c + dc

        #             if (0 <= nr < rows and 0 <= nc < cols and 
        #                 grid[nr][nc] == '1' and (nr, nc) not in visited):
        #                 visited.add((nr, nc))
        #                 queue.append((nr, nc))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1' and (r, c) not in visited:
        #             islands += 1
        #             bfs(r, c)
                    
        # return islands


        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        def bfs(r,c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()

                for deltaR, deltaC in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr = curr_r + deltaR
                    nc = curr_c + deltaC

                    if (0<=nr<rows and 0<=nc<cols and
                        grid[nr][nc]=='1' and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count +=1
                    bfs(r,c)
        return count
                    




















