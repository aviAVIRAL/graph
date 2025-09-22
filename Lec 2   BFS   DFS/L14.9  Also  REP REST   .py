

# first preferences  DFS


# first preferences 
 
def dfs(row, col, vis, mat, n, m):
    
    vis[row][col] = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for delrow, delcol in directions:
        nrow, ncol = row + delrow, col + delcol
        if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
            dfs(nrow, ncol, vis, mat, n, m)

def Function(n, m, mat):
    # delrow = [-1, 0, 1, 0] # I AM NOT GIVING RFIRST PREFERENCE TO THIS BHAI 
    # delcol = [0, 1, 0, -1] 
    vis = [[0] * m  for _ in range(n)]

    # -------------------------------------------------------
    # Traverse first and last row
    for j in range(m):
        if not vis[0][j] and mat[0][j] == 'O':
            dfs(0, j, vis, mat, n, m)
        if not vis[n-1][j] and mat[n-1][j] == 'O':
            dfs(n-1, j, vis, mat, n, m)
    
    # Traverse first and last column
    for i in range(n):
        if not vis[i][0] and mat[i][0] == 'O':
            dfs(i, 0, vis, mat, n, m)
        if not vis[i][m-1] and mat[i][m-1] == 'O':
            dfs(i, m-1, vis, mat, n, m)
    # -------------------------------------------------------    
    
    # Convert unvisited 'O' to 'X'
    for i in range(n):                                                                                               
        for j in range(m):
            if not vis[i][j] and mat[i][j] == 'O':
                mat[i][j] = 'X'
    
    return mat

# Example usage
mat = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

ans = Function(5, 4, mat)
for row in ans:
    print(*row)
