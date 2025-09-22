
# BFS

from collections import deque

from collections import deque

# BFS to mark reachable land from the boundary
def bfs(row, col, vis, grid, n, m):
    q = deque()
    q.append((row, col))
    vis[row][col] = 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nrow, ncol = r + dr, c + dc
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                vis[nrow][ncol] = 1
                q.append((nrow, ncol))

# Function to count number of enclaves
def number_of_enclaves(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]

    # Run BFS for all boundary land cells- T R I CK 
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1 and not vis[i][j]:
                bfs(i, j, vis, grid, n, m)

    # Count unvisited land cells
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not vis[i][j]:
                cnt += 1

    return cnt

# Example usage
grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

print("Number of enclaves:", number_of_enclaves(grid))