class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        time = 0
        while queue:
            x, y, t = queue.popleft()
            time = max(time, t)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2 
                    fresh -= 1
                    queue.append((nx, ny, t + 1))
        return time if fresh == 0 else -1
        