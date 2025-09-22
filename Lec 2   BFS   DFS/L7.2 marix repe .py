

# NO of provicense

def dfs(node, AdjaMat, vis, n):
    vis[node] = 1
    for neighbor in range(n):
        if AdjaMat[node][neighbor] == 1 and not vis[neighbor]:
            dfs(neighbor, AdjaMat, vis, n)

def num_provinces(AdjaMat, n):
    vis = [0] * n
    count = 0
    for i in range(n):
        if not vis[i]:
            count += 1
            dfs(i, AdjaMat, vis, n)
    return count

if __name__ == "__main__":
    # AdjaMatacency matrix input  #AdjaMata matrix ki form mein given hai bhai AdjaMatecency 
    AdjaMat = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    n = len(AdjaMat)     # totoal node edges 
    print(num_provinces(AdjaMat, n))

  