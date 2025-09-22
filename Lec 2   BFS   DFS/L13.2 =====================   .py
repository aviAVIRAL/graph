

# aslo rep   # first preferences 

from collections import deque

def nearest(grid):
    n = len(grid)
    m = len(grid[0])
    vis = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0)) # aslo rep # first prefe
                vis[i][j] = 1
    
    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]
     
    while q:
        row, col, steps = q.popleft() # aslo rep
        dist[row][col] = steps
        
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol]:
                vis[nrow][ncol] = 1
                q.append(( nrow, ncol, steps + 1))
    
    return dist

# # Example usage
# grid = [
#     [0, 1, 1, 0],
#     [1, 1, 0, 0],
#     [0, 0, 1, 1]
# ]

# ans = nearest(grid)
# for row in ans:
#     print(" ".join(map(str, row)))

print()# Example usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]
                ## op dist
#    2 1 2
#    1 0 1
#    0 1 0
 
ans = nearest(grid)
for row in ans:
    print(*row)
    # print(" ".join(map(str, row))) # also rep 

# -----------------------



from collections import deque

def nearest(grid):
    n = len(grid)
    m = len(grid[0])

    vis = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append(((i, j), 0))
                vis[i][j] = 1
    
    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]
    
    while q:
        (row, col), steps = q.popleft()
        dist[row][col] = steps
        
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol]:
                vis[nrow][ncol] = 1
                q.append(((nrow, ncol), steps + 1))
    
    return dist

# Example usage
grid = [
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

ans = nearest(grid)
for row in ans:
    print(" ".join(map(str, row)))

print()# Example usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]
                 # #     o p 
#    2 1 2
#    1 0 1
#    0 1 0
 

ans = nearest(grid)
for row in ans:
    print(" ".join(map(str, row)))

