from typing import List

class Solution:
    def dfs(self, row: int, col: int, Copyi: List[List[int]], image: List[List[int]], 
            newColor: int, directions: List[tuple], iniColor: int) -> None:

        Copyi[row][col] = newColor  
        n, m = len(image), len(image[0])  

        for dx, dy in directions:
            nrow = row + dx
            ncol = col + dy

            if (0 <= nrow < n and 0 <= ncol < m and 
                image[nrow][ncol] == iniColor and 
                Copyi[nrow][ncol] != newColor):
                self.dfs(nrow, ncol, Copyi, image, newColor, directions, iniColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        iniColor = image[sr][sc]  
        Copyi = [row for row in image]  # Shallow copy (same as your version)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

        self.dfs(sr, sc, Copyi, image, newColor, directions, iniColor)  
        return Copyi

# === Original Test Case ===
image1 = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

obj = Solution()
Ans = obj.floodFill(image1, 1, 1, 2)
for row in Ans:
    print(*row)
