



# optimize  IMpo 

from collections import deque

def bfs(row, col, grid):
    n, m = len(grid), len(grid[0])

    q = deque()
    q.append((row, col, 'S'))  # Start marker

    grid[row][col] = '0'

    path = []

    directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]

    while q:
        r, c, move = q.popleft()
        path.append(move)

        for dr, dc, dir_char in directions:
            nrow, ncol = r + dr, c + dc
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1':
                grid[nrow][ncol] = '0'
                q.append((nrow, ncol, dir_char))

        path.append('B')  # Backtrack

    return ''.join(path)

def num_unique_islands(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    shapes = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                shape_code = bfs(i, j, grid)
                shapes.add(shape_code)

    return len(shapes)


grid = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0']
]

print(num_unique_islands(grid))  # Output: 2
