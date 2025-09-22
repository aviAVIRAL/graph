from collections import deque

def bfs(sr, sc, grid, n, m):

    q = deque()
    q.append((sr, sc))
    
    grid[sr][sc] = 'T'  # ----------

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        r, c = q.popleft()
        for delrow, delcol in directions:
            nrow, ncol = r + delrow, c + delcol
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 'O':
                grid[nrow][ncol] = 'T'
                q.append((nrow, ncol))

def replaceowithx(n, m, grid):
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and grid[i][j] == 'O':
                bfs(i, j, grid, n, m)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':  # ----------
                grid[i][j] = 'X'
            elif grid[i][j] == 'T':
                grid[i][j] = 'O'

    return grid

grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

ans = replaceowithx(5, 4, grid)
for row in ans:
    print(*row)
