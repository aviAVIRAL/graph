from collections import deque

def bfs(sr, sc, image, newColor, directions, iniColor):
    image[sr][sc] = newColor  # ---------------------------
    n, m = len(image), len(image[0])
    q = deque()
    q.append((sr, sc))

    while q:
        row, col = q.popleft()
        for dx, dy in directions:
            nrow = row + dx
            ncol = col + dy

            if (0 <= nrow < n and 0 <= ncol < m and
                image[nrow][ncol] == iniColor): # -------------------------------

                image[nrow][ncol] = newColor
                q.append((nrow, ncol))

def floodFill(image, sr, sc, newColor):
    iniColor = image[sr][sc]

    if iniColor == newColor:
        return image  # no need to fill if same color

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    bfs(sr, sc, image, newColor, directions, iniColor)
    return image

# === Original Test Case ===
print("Original Test Case:")
image1 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
result1 = floodFill(image1, 1, 1, 2)
for row in result1:
    print(*row)

# === Additional Test Case (Start from 0) ===
print("\nTest Case Starting from 0:")
image2 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
result2 = floodFill(image2, 2, 1, 9)
for row in result2:
    print(*row)
