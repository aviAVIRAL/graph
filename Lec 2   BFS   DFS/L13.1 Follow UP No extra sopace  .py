

# follow up no extra spac  Dist + vis remove 


from collections import deque

def bfs(q, grid, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        row, col = q.popleft()

        for dx, dy in directions:
            nrow = row + dx
            ncol = col + dy

            # Only visit unvisited cells marked as -1
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == -1:
                
                grid[nrow][ncol] = grid[row][col] + 1
                q.append((nrow, ncol))

    return grid

def Function(grid):
    n = len(grid)
    m = len(grid[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j))
                grid[i][j] = 0  # distance to itself
            else:
                grid[i][j] = -1  # mark as unvisited

    return bfs(q, grid, n, m)

# Example
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

ans = Function(grid)
for row in ans:
    print(*row)

