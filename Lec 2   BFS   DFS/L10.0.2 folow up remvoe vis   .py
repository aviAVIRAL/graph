


# remov visxt extra space  

from collections import deque

def bfs(grid, q):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    maxTime = 0

    while q:
        r, c, t = q.popleft()
        maxTime = max(maxTime, t)

        for dx, dy in directions:
            nr, nc = r + dx, c + dy

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                
                grid[nr][nc] = 2  # Mark fresh orange as rotten 
                q.append((nr, nc, t + 1))


    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1  : # ek bee fresh orange present hai 
                return -1
    return maxTime

    # for row in grid:
    #     if 1 in row:
    #         return -1

    # return maxTime

def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))

    return bfs(grid, q)

# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

rotting_time = orangesRotting(grid)
print("Minimum Number of Minutes Required:", rotting_time)
