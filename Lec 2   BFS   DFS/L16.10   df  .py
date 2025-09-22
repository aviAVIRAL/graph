def dfs(row, col, vis, grid, n, m, path, direction):
    vis[row][col] = 1
    path.append(direction)

    directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]

    for dr, dc, dir_char in directions:
        nrow, ncol = row + dr, col + dc
        if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
            dfs(nrow, ncol, vis, grid, n, m, path, dir_char)

    path.append('B')  # Mark backtracking

def num_unique_islands(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    unique_shapes = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not vis[i][j]:
                path = []
                dfs(i, j, vis, grid, n, m, path, 'S')  # 'S' = start
                unique_shapes.add(''.join(path))

    return len(unique_shapes)
grid = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0']
]

print(num_unique_islands(grid))  # Output: 2
