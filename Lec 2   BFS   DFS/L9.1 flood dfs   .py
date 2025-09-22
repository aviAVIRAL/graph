


from typing import List

def dfs(row: int, col: int, Copyi: List[List[int]], image: List[List[int]], 
        newColor: int, directions: List[tuple], iniColor: int) -> None:

    
    Copyi[row][col] = newColor  

    n, m = len(image), len(image[0])  

    for dx, dy in directions:
        nrow = row + dx
        ncol = col + dy
        
        if (0 <= nrow < n and 0 <= ncol < m and 
            image[nrow][ncol] == iniColor and 
            Copyi[nrow][ncol] != newColor):
            dfs(nrow, ncol, Copyi, image, newColor, directions, iniColor)
 
def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    
    iniColor = image[sr][sc]  
    
    Copyi = [row   for row in image]  
    # Copyi = [row[:] for row in image]  

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    dfs(sr, sc, Copyi, image, newColor, directions, iniColor)  
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

# output 
# 2 2 2
# 2 2 0
# 2 0 1

# === Additional Test Case (Start from 0) ===
print("\nTest Case Starting from 0:")
image2 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]      # ---------IMP  o col will change  into 9 ----
]
Copyi2 = floodFill(image2, 2, 1, 9)
for row in Copyi2:
    print(*row)
# output 

# Test Case Starting from 0:
# 1 1 1
# 1 1 0
# 1 9 1