 
# numbe rof unique island 

# DFS 
 
# numbe of unique island 

# DFS 

def dfs(row, col, vis, mat, Base_row, Base_col, shape):
    n, m = len(mat), len(mat[0])
    vis[row][col] = 1       

    shape.append((row - Base_row, col - Base_col))

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    for deltrow, deltcol in directions:
        nrow = row + deltrow
        ncol = col + deltcol

# aslo rep  
# if (0 <= new_row < n and 0 <= new_col < m :
# if (new_row >=0 and new_row < n and new_col >= 0 and new_col < m :
        if 0<=nrow<n and 0<=ncol<m and mat[nrow][ncol] == '1' and not vis[nrow][ncol]:
            dfs(nrow,ncol,vis,mat, Base_row, Base_col, shape)

def num_unique_islands(mat):
    n, m = len(mat), len(mat[0])
    vis = [[0] * m for _ in range(n)]
    st = set()
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '1' and not vis[i][j]:
                shape = []
                dfs(i, j, vis, mat, i, j, shape)
                # st.add(frozenset(shape))   
                st.add(tuple(shape))  # also use 
      #          st.add(shape) #  wrong ans 

    return len(st)

# Example usage

mat = [
    ['1', '1', '0', '1', '1'],
    ['1', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '1'],
    ['1', '1', '0', '1', '0']
]

print(num_unique_islands(mat))

# output 
# st = 
# {   frozenset({(0, 1), (1, 0), (0, 0)}),    
#     frozenset({(0, 1), (0, 0)})            }  


