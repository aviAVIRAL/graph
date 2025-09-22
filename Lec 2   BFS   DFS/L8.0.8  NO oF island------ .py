

# rows, cols = len(grid), len(grid[0])
# vis = [[0] * cols for _ in range(rows)]


vis = [[0]*4  for _ in range(4)]
print(vis)

grid = [[1,3,2], [9,3,2]]

print()
print()

rows = len(grid)
cols = len(grid[0])
vis = [[0] * cols for _ in range(rows)]

for x in vis : 
    print(*x)
print()


# all direction  

    # (-1, -1)   (-1, 0)   (-1, 1)
    #    ↖         ↑         ↗  
    # ( 0, -1)    (i, j)   ( 0, 1)
    #    ←         🟢         →  
    # ( 1, -1)   ( 1, 0)   ( 1, 1)
    #    ↙         ↓         ↘  

