class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        fresh = 0
        mins = 0
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        while rotten and fresh > 0:
            for l in range(len(rotten)):
                r , c = rotten.popleft()
                for k in range(4):
                    rr = r + dx[k]
                    cc = c + dy[k]
                    if rr >= 0 and cc >= 0 and rr < rows and cc < cols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh -= 1
                        rotten.append((rr,cc))
            mins += 1
        return mins if fresh == 0 else -1
