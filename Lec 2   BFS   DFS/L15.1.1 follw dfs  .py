


def dfs(row, col, grid, n, m):

    grid[row][col] = -1  # ---------------------
#    grid[row][col] = 0   Simople ahi --------------------  also rep 
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for dr, dc in directions:
        nrow, ncol = row + dr, col + dc
        if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
            dfs(nrow, ncol, grid, n, m)

def number_of_enclaves(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1:
                dfs(i, j, grid, n, m)

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
