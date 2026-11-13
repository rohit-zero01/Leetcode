from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build the adjacency list first
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        # Calculate in-degree for all vertices using your loop
        indegree = [0] * numCourses
        for u in range(numCourses):
            for v in adj[u]:
                indegree[v] += 1

        # Add courses with 0 in-degree to the queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # Process the queue
        count = 0
        while queue:
            u = queue.popleft()
            count += 1
            
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        # If count matches numCourses, no cycle exists
        return count == numCourses
