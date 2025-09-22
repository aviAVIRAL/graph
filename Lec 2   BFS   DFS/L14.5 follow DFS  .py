



def dfs(row, col, grid, n, m):
    grid[row][col] = 'T'  # mark visited temporarily
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for delrow, delcol in directions:
        nrow, ncol = row + delrow, col + delcol
        if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 'O':
            dfs(nrow, ncol, grid, n, m)

def replace(n, m, grid):
    for i in range(n):
        for j in range(m):
            # Start DFS only from 'O's on the border
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and grid[i][j] == 'O':
                dfs(i, j, grid, n, m)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                grid[i][j] = 'X'  # surrounded region
            elif grid[i][j] == 'T':
                grid[i][j] = 'O'  # revert temporary mark back

    return grid

grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

ans = replace(5, 4, grid)
for row in ans:
    print(*row)
