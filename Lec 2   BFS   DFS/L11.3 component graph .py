
# Cycle Detection in unirected Graph (bfs)

from collections import deque

def detect(Start, adj, vis):
    q = deque([(Start, -1)])  
    vis[Start] = 1  
       
    while q:
        node, parent = q.popleft()  
        for neighbor in adj[node]:
            if not vis[neighbor]:
                q.append((neighbor, node))  
                vis[neighbor] = 1  
            elif neighbor != parent :
                return True  
    return False  

# def isCycle(V, adj):      # single graph 
#     vis = [0] * V 
#     startNode = 1 
#     return detect(startNode, adj, vis)

def isCycle(V, adj):  # component graph 
    vis = [0] * V  
    for startNode in range(V):     
        if not vis[startNode]:  
            if detect(startNode, adj, vis):
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

