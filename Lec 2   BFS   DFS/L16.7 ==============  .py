


 


# dfs 


def dfs_check(node, adj, vis, path_vis):
    vis[node] = 1
    path_vis[node] = 1

    # Traverse adjacent nodes
    for neighbor in adj[node]:
        # If not visited, r   ecursively call DFS
        if not vis[neighbor]:
            if dfs_check(neighbor, adj, vis, path_vis):
                return True
        # If the node is already in the current path, cycle detected
        elif path_vis[neighbor] == 1:
            return True

    path_vis[node] = 0  # Backtrack
    return False

def is_cyclic(V, adj):
    vis = [0] * V  # Visited array
    path_vis = [0] * V  # Path visited array

    for i in range(V):  # Check for each component
        if not vis[i]:
            if dfs_check(i, adj, vis, path_vis):
                return True

    return False

# Example usage
V = 11
adj = [[], [2], [3], [4, 7], [5], [6], [], [5], [9], [10], [8]]

print("True" if is_cyclic(V, adj) else "False")
