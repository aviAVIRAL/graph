
# first prefernces ----DFS 

def dfs(row, col, vis, grid, n, m):
    vis[row][col] = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for delrow, delcol in directions:
        nrow, ncol = row + delrow, col + delcol
        if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and grid[nrow][ncol] == 'O':
            dfs(nrow, ncol, vis, grid, n, m)

def ReplaceZeroWuthX(n, m, grid):
    vis = [[0] * m for _ in range(n)]

    # # -------------------------------------------------------
    # # Traverse first and last row
    # for j in range(m):
    #     if not vis[0][j] and grid[0][j] == 'O':
    #         dfs(0, j, vis, grid, n, m)
    #     if not vis[n-1][j] and grid[n-1][j] == 'O':
    #         dfs(n-1, j, vis, grid, n, m)
    
    # # Traverse first and last column
    # for i in range(n):
    #     if not vis[i][0] and grid[i][0] == 'O':
    #         dfs(i, 0, vis, grid, n, m)
    #     if not vis[i][m-1] and grid[i][m-1] == 'O':
    #         dfs(i, m-1, vis, grid, n, m)
    # # -------------------------------------------------------    
# WI TH TRICK          # first rep oreferences 
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and grid[i][j] == 'O' and not vis[i][j]:
                dfs(i, j, vis, grid, n, m)
    # # -------------------------------------------------------    
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

ans = ReplaceZeroWuthX(5, 4, grid)
for row in ans:
    print(*row)