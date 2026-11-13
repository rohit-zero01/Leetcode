from collections import deque

class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Build the adjacency list
        adj = [[] for _ in range(n)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        # Calculate in-degree for all vertices
        indegree = [0] * n
        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1

        # 2. Add all vertices with in-degree 0 to the queue
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

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
