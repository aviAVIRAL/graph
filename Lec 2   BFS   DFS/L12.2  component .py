

# Detect Cycle in an Undirected Graph (using DFS)

def dfs(node, parent, vis, adj):
    vis[node] = 1  
    for ngr in adj[node]:
        if not vis[ngr]:  
            if dfs(ngr, node, vis, adj):
                return True  
        elif ngr != parent:  
            return True  
    return False  

def isCycle(V, adj):
    vis = [0] * V  
    for StartingNode in range(V):  
        if not vis[StartingNode]:  
            if dfs(StartingNode, -1, vis, adj):
                return True  
    return False  


if __name__=="__main__":
    adj = [[], [2], [1, 3], [2]] 
    V = 4 
    print(isCycle(V, adj))

if __name__=="__main__":
    adj = [[], [2], [1, 3], [2, 1]] 
    V = 4 
    print(isCycle(V, adj))
