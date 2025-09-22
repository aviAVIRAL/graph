

from collections import deque

def bfs(startNode, color, adj):
    
    queue = deque([startNode])
    color[startNode] = 0
    
    while queue:
        node = queue.popleft()
        for ngbr in adj[node]:
            if color[ngbr] == -1:
                color[ngbr] = 1 - color[node]
                queue.append(ngbr)
            elif color[ngbr] == color[node]:
                return False
    return True

def is_bipartite_from_node_zero(V, adj):
    color = [-1] * V 
    StrN = 0  
    if bfs(StrN, color, adj) == False: 
        return False   # Not bipartite
    return True         # ✅ Must return True explicitly if bipartite

if __name__ == '__main__':
    V = 4
    Edges = [(0, 2), (0, 3), (2, 3), (3, 1)]

    adj = [[] for _ in range(V)]
    for u, v in Edges:
        adj[u].append(v)
        adj[v].append(u)

    print(1 if is_bipartite_from_node_zero(V, adj) else 0)
