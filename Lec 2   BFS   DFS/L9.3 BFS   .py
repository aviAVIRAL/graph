from collections import deque

def bfs(sr, sc, Copyi, image, newColor, directions, iniColor):
    Copyi[sr][sc] = newColor
    n, m = len(image), len(image[0])
    q = deque()
    q.append((sr, sc))

    while q:
        row, col = q.popleft()
        for dx, dy in directions:
            nrow = row + dx
            ncol = col + dy

            if (0 <= nrow < n and 0 <= ncol < m and
                image[nrow][ncol] == iniColor and
                Copyi[nrow][ncol] != newColor):

                Copyi[nrow][ncol] = newColor
                q.append((nrow, ncol))

def floodFill(image, sr, sc, newColor):
    iniColor = image[sr][sc]
    
    # Deep copy of image
    Copyi = [row[:] for row in image]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    bfs(sr, sc, Copyi, image, newColor, directions, iniColor)
    return Copyi

# === Original Test Case ===
print("Original Test Case:")
image1 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
Copyi1 = floodFill(image1, 1, 1, 2)
for row in Copyi1:
    print(*row)

# === Additional Test Case (Start from 0) ===
print("\nTest Case Starting from 0:")
image2 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
Copyi2 = floodFill(image2, 2, 1, 9)
for row in Copyi2:
    print(*row)
