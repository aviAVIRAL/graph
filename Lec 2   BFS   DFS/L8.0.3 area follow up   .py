from collections import deque

# follow up : fimd the area + maximum are of island

# vistsed   mat use kr + area be nikal 

# ----------------------------------------------------------- 

def bfs(grid, i, j):
    area = 1  # Start with current cell ----------Impo---------------
    grid[i][j] = '0'  # Mark as visited
    q = deque([(i, j)])
    n, m = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   

    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                grid[nr][nc] = '0'
                q.append((nr, nc))
                area += 1  # Count cell as part of island  -----Impo------
    return area

def island_areas(grid):
    if not grid:
        return []

    AREAS = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                area = bfs(grid, i, j)
                AREAS.append(area)
    return AREAS


grid1 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

areas = island_areas(grid1)
print("Island areas:", areas)
print("Largest island area:", max(areas) if areas else 0)
