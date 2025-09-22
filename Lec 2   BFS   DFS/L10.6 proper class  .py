from collections import deque
from typing import List

def get_initial_state(grid: List[List[int]]) :
    """Find all rotten oranges and count the total number of oranges."""
    rotten = deque()
    total = 0
    n, m = len(grid), len(grid[0])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                total += 1
            if grid[i][j] == 2:
                rotten.append((i, j))
    
    return rotten, total

def spread_rot(grid: List[List[int]], rotten: deque) -> int:
    """Perform BFS to spread rot to fresh oranges and return time taken."""
    n, m = len(grid), len(grid[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    days, count = 0, 0
    
    while rotten:
        k = len(rotten)
        count += k
        for _ in range(k):
            x, y = rotten.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    rotten.append((nx, ny))
        
        if rotten:
            days += 1
    
    return days, count

def orangesRotting(grid: List[List[int]]) -> int:
    """Main function to calculate the minimum number of minutes required."""
    if not grid:
        return 0

    rotten, total = get_initial_state(grid)
    days, count = spread_rot(grid, rotten)

    return days if total == count else -1

# Example usage
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
rotting_time = orangesRotting(grid)
print("Minimum Number of Minutes Required:", rotting_time)
