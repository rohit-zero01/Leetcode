from collections import deque

class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Build the adjacency list and in-degree array
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        # Note: Input is typically [dest, src], meaning src -> dest
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
            
        # 2. Add all tasks with no prerequisites to the queue
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        
        # 3. Process the queue
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    
        # 4. If order contains all tasks, return it; otherwise, cycle exists
        return topo_order if len(topo_order) == n else []
