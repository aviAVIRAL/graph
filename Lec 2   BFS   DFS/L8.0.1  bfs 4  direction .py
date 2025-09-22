from collections import deque

def bfs(grid, i, j, vis):
    vis[i][j] = 1
    q = deque([(i, j)])
    n = len(grid)
    m = len(grid[0])
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    while q:
        row, col = q.popleft()
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy

            if (0 <= new_row < n and
                0 <= new_col < m and
                grid[new_row][new_col] == '1' and not vis[new_row][new_col]): 
                
                vis[new_row][new_col] = 1
                q.append((new_row, new_col))

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    vis = [[0] * cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if not vis[i][j] and grid[i][j] == '1':
                bfs(grid, i, j, vis)
                count += 1
    return count

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(num_islands(grid))
