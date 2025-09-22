from collections import deque

def bfs(row, col, vis, grid, n, m):
    q = deque()
    q.append((row, col))
    vis[row][col] = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        r, c = q.popleft()
        for delrow, delcol in directions:
            nrow, ncol = r + delrow, c + delcol
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and grid[nrow][ncol] == 'O':
                vis[nrow][ncol] = 1
                q.append((nrow, ncol))

def replaceOwithX(n, m, grid):
    vis = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and grid[i][j] == 'O' and not vis[i][j]:
                bfs(i, j, vis, grid, n, m)

    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] == 'O':
                grid[i][j] = 'X'

    return grid

grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

ans = replaceOwithX(5, 4, grid)
for row in ans:
    print(*row)
