 
# seprate function haui ismein 


from collections import deque

def bfs(grid, vis, q):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    maxTime = 0

    while q:
        r, c, t = q.popleft()
        maxTime = max(maxTime, t)

        for dx, dy in directions:
            nRow, nCol = r + dx, c + dy

            if (0 <= nRow < n and 0 <= nCol < m and
                grid[nRow][nCol] == 1 and not vis[nRow][nCol] ):
                # grid[nRow][nCol] == 1 and not vis[i][j] ) : 
                
                q.append((nRow, nCol, t + 1))
                vis[nRow][nCol] = 2

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not vis[i][j] :
            # if grid[i][j] == 1 and not vis[i][j] :
                return -1
    return maxTime


def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
                vis[i][j] = 2
            elif grid[i][j] == 1:
                vis[i][j] = 0

    ans = bfs(grid, vis, q)

    return ans


# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

rotting_time = orangesRotting(grid)
print("Minimum Number of Minutes Required:", rotting_time)