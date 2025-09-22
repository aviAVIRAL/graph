 
# numbe rof unique island 

# DFS 

def dfs(row, col, vis, MATRIX, base_row, base_col, shape):
    n, m = len(MATRIX), len(MATRIX[0])
    vis[row][col] = 1       

    shape.append( [row - base_row, col - base_col] )

    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]
    
    for i in range(4):
        nrow = row + delrow[i]
        ncol = col + delcol[i]
# aslo rep  
# if (0 <= new_row < n and 0 <= new_col < m :
# if (new_row >=0 and new_row < n and new_col >= 0 and new_col < m :
        if 0<=nrow<n and 0<=ncol<m and MATRIX[nrow][ncol] == '1' and not vis[nrow][ncol]:
            dfs(nrow,ncol,vis,MATRIX, base_row, base_col, shape)

def num_unique_islands(MATRIX):
    n, m = len(MATRIX), len(MATRIX[0])
    vis = [[0] * m for _ in range(n)]
    st = set()
    
    for i in range(n):
        for j in range(m):
            if MATRIX[i][j] == '1' and not vis[i][j]:
                shape = []
                dfs(i, j, vis, MATRIX, i, j, shape)
                st.add(frozenset(shape))   
                # st.add(tuple(shape))  # also use 
      #          st.add(shape) #  wrong ans 

    return len(st)

# Example usage

MATRIX = [
    ['1', '1', '0', '1', '1'],
    ['1', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '1'],
    ['1', '1', '0', '1', '0']
]

print(num_unique_islands(MATRIX))

# output 
# st = 
# {   frozenset({(0, 1), (1, 0), (0, 0)}),    
#     frozenset({(0, 1), (0, 0)})            }  


