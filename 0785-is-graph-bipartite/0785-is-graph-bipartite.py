from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1]*n

        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0

                while queue:
                    u = queue.popleft()

                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1-color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        
        return True
# from collections import deque

# class Solution:
#     def isBipartite(self, graph: list[list[int]]) -> bool:
#     # graph is an adjacency list representation
#         n = len(graph)
#         color = [-1] * n

#         # Iterate through each node to handle disconnected components
#         for i in range(n):
#             if color[i] == -1:
#                 # Start BFS for this component
#                 queue = deque([i])
#                 color[i] = 0
                
#                 while queue:
#                     u = queue.popleft()
                    
#                     for v in graph[u]:
#                         # If neighbor is not colored, assign opposite color
#                         if color[v] == -1:
#                             color[v] = 1 - color[u]
#                             queue.append(v)
#                         # If neighbor has the same color, it's not bipartite
#                         elif color[v] == color[u]:
#                             return False
                            
#         return True



        