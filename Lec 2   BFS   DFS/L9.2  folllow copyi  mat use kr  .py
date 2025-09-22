

def dfs(row, col, image, newColor, iniColor):

    image[row][col] = newColor # impo -----------------

    n, m = len(image), len(image[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  

    for dx, dy in directions:
        nrow = row + dx
        ncol = col + dy

        if (0 <= nrow < n and 0 <= ncol < m and
            image[nrow][ncol] == iniColor):
            
            dfs(nrow, ncol, image, newColor, iniColor)

def floodFill(image, sr, sc, newColor):

    iniColor = image[sr][sc]

    if iniColor == newColor:
        return image

    dfs(sr, sc, image, newColor, iniColor)
    return image

# ✅ Test Case
image = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

result = floodFill(image, 1, 1, 2)

# Print result
for row in result:
    print(*row)
