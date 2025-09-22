def dfs(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    grid[i][j] = '0'
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_row = i + dx
        new_col = j + dy
        if (0 <= new_row < n and
            0 <= new_col < m and
            grid[new_row][new_col] == '1'):
            dfs(grid, new_row, new_col)

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(num_islands(grid))  # Output: 3
