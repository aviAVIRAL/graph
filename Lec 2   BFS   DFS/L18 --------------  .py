
# D F S  

def dfs(node, col,        color, adj):
    color[node] = col
    for neighbor in adj[node]:
        if color[neighbor] == -1:
            # if not dfs(neighbor, 1 - col, color, adj):return False # also rep
            # if not dfs(neighbor, not col, color, adj): return False # also rep as
            if dfs(neighbor, 1 - col, color, adj) == False : 
                return False   

        elif color[neighbor] == color[node]:
            return False
    return True

def is_bipartite(V, adj):
    color = [-1] * V   # component graph 
    for start in range(V):  # Handle disconnected graphs 
        if color[start] == -1:
         # starting_Node ,Col o: Yelow , 1: Red   
            # if not dfs(start, 0,    color, adj): return False # aslo rep 
            if dfs(start, 0,    color, adj) == False: 
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





