from collections import deque

def bfs(grid, vis, q, fresh):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0
    cnt = 0

    while q:
        r, c, t = q.popleft()
        time = max(time, t)

        for dx, dy in directions:
            nRow, nCol = r + dx, c + dy

            if (0 <= nRow < n and 0 <= nCol < m and
                grid[nRow][nCol] == 1 and not vis[nRow][nCol]  ):

                q.append((nRow, nCol, t + 1))
                vis[nRow][nCol] = 2
                cnt += 1

    if cnt == fresh : return time 
    else : return -1

def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    q = deque()
    fresh = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
                vis[i][j] = 2
            elif grid[i][j] == 1:
                fresh += 1

    return bfs(grid, vis, q, fresh)

# ✅ Test Case
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print("Minimum Number of Minutes Required:", orangesRotting(grid))
