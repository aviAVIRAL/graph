from collections import deque

def bfs(row, col, grid, base_row, base_col, shape):
    n, m = len(grid), len(grid[0])
    grid[row][col] = '0'  # mark visited by changing '1' to '0'
    q = deque([(row, col)])
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    
    while q:
        r, c = q.popleft()
        shape.append((r - base_row, c - base_col))

        for deltrow, deltcol in directions:
            nrow, ncol = r + deltrow, c + deltcol
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1':
                grid[nrow][ncol] = '0'  # mark visited
                q.append((nrow, ncol))

def num_unique_islands(grid):
    n, m = len(grid), len(grid[0])
    shapes = set()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                shape = []
                bfs(i, j, grid, i, j, shape)
                shapes.add(tuple(shape))
    
    return len(shapes)

grid = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0']
]

print(num_unique_islands(grid))
