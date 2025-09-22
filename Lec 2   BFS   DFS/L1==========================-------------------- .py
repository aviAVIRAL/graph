 
def dfs( node, adjLs, vis):
    vis[node] = True
    for neighbor in adjLs[node]:
        if not vis[neighbor]:
            dfs(neighbor, adjLs, vis)

def num_provinces(edge, n):
 
    vis = [0] * n
    count = 0

    for i in range(n):
        if not vis[i]:
            count += 1
            dfs( i, adjLs, vis)
    return count
