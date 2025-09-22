

# fololow up space vis not use 

from collections import deque

def bfs(row, col, grid, n, m):
    q = deque()
    q.append((row, col))
    grid[row][col] = -1  # mark as visited
    # grid[row][col] = 0  # mark as visited

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nrow, ncol = r + dr, c + dc
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
                grid[nrow][ncol] = -1
                q.append((nrow, ncol))

def number_of_enclaves(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1:
                bfs(i, j, grid, n, m)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt += 1

    return cnt

grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

print("Number of enclaves:", number_of_enclaves(grid))
