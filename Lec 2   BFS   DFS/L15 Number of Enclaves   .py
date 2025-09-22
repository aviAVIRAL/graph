from collections import deque

def number_of_enclaves(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    q = deque()
    
    # Traverse boundary elements
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                if grid[i][j] == 1:
                    q.append((i, j))
                    vis[i][j] = 1
    
    delrow = [-1, 0, 1, 0]  # old representation -------------------
    delcol = [0, 1, 0, -1]
    
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow, ncol = row + delrow[i], col + delcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                q.append((nrow, ncol))
                vis[nrow][ncol] = 1
    
    # cnt = sum(grid[i][j] == 1 and not vis[i][j] for i in range(n) for j in range(m))
    cnt = 0  # Initialize count
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not vis[i][j]:  
                cnt += 1  # Increment count if the condition is met

    return cnt

# Example usage
grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

print(number_of_enclaves(grid))
