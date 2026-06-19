class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        dx = [0,0,1,-1]
        dy = [1,-1, 0 ,0]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            
            grid[r][c] = 0

            for k in range(4):
                rr = r + dx[k]
                cc = c + dy[k]
                dfs(rr,cc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        
        return islands