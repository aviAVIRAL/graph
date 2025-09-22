 
from collections import deque

def bfs(row, col, vis, grid):
    n, m = len(grid), len(grid[0])
    vis[row][col] = 1
    q = deque([(row, col)])
    
    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]

    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow, ncol = row + delrow[i], col + delcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                vis[nrow][ncol] = 1
                q.append((nrow, ncol))

def num_islands(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    count = 0  # ye cnt ko optize kr diya hai bus yahee 
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not vis[i][j]:
                count += 1
                bfs(i, j, vis, grid)
    
    return count  # ye cnt ko optize kr diya hai bus yahee 

# Example usage
grid = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0']
]

print(num_islands(grid))

