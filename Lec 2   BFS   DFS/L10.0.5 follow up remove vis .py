from collections import deque

def bfs(grid, q, fresh):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0
    cnt = 0

    while q:
        r, c, t = q.popleft()
        time = max(time, t)

        for dx, dy in directions:
            nRow, nCol = r + dx, c + dy

            if (0 <= nRow < n and 0 <= nCol < m and grid[nRow][nCol] == 1):
                
                q.append((nRow, nCol, t + 1))
                grid[nRow][nCol] = 2  # Mark as rotten directly in grid
                cnt += 1

    return time if cnt == fresh else -1

def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1

    return bfs(grid, q, fresh)

# ✅ Test Case
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print("Minimum Number of Minutes Required:", orangesRotting(grid))
