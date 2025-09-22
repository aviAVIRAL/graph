from collections import deque

def bfs(q, vis, dist, grid, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        row, col, steps = q.popleft()
        dist[row][col] = steps

        for dx, dy in directions:
            nrow, ncol = row + dx, col + dy
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 0 and not vis[nrow][ncol]:
                vis[nrow][ncol] = 1
                q.append((nrow, ncol, steps + 1))

    return dist

def Function(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                vis[i][j] = 1

    return bfs(q, vis, dist, grid, n, m)

# Test Case
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

ans = Function(grid)
for row in ans:
    print(*row)
