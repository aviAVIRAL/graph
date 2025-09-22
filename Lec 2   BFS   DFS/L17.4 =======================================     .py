
 

from collections import deque

def is_bipartite(V, adj):
    color = [-1] * V
                        # leetcode repre Neste function ki form mein 
    def bfs(start):
        queue = deque([start])  
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # color[neighbor] = not color[node]  #  impo  aslo repe  
                    color[neighbor] = 1 - color[node] # impo  aslo repe as 
                        # if color[node] == 1 : color[neighbor] = 0 
                        # if color[node] == 0 : color[neighbor] = 1 
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for i in range(V):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True
if __name__ == '__main__':
    V = 4
    Edges = [(0, 2), (0, 3), (2, 3), (3, 1)]
    adj = [[] for _ in range(V)]
    for u, v in Edges:
        adj[u].append(v)
        adj[v].append(u)

    print(1 if is_bipartite(V, adj) else 0)

# [[2, 3], [3], [0, 3], [0, 2, 1]]

# 0 → 2, 3
# 1 → 3
# 2 → 0, 3
# 3 → 0, 2, 1