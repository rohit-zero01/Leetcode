from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # n = len(graph)
        # color = [-1]*n

        # for i in range(n):
        #     if color[i] == -1:
        #         queue = deque([i])
        #         color[i] = 0
        #                                 #BFS
        #         while queue:
        #             u = queue.popleft()

        #             for v in graph[u]:
        #                 if color[v] == -1:
        #                     color[v] = 1-color[u]
        #                     queue.append(v)
        #                 elif color[v] == color[u]:
        #                     return False
        
        # return True


        n = len(graph)
        color = [-1] * n 

        def dfs(node, col):
            color[node] = col

            for v in graph[node]:
                if color[v] == -1:
                    if not dfs(v, 1 - col):
                        return False
                    
                elif color[v] == col:
                    return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        return True



