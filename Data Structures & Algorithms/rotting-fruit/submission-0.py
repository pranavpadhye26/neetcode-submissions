class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        rows = len(grid)
        cols = len(grid[0])
        mins = 0
        dx = [1, -1 , 0 , 0]
        dy = [0 , 0 , 1 , -1]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for k in range(4):
                    nr = r + dx[k]
                    nc = c + dy[k]
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.append((nr,nc))
                        fresh -= 1
            mins += 1
        return mins if fresh == 0 else -1
                


