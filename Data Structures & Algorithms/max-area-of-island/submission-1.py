class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.dx = [0,0,1,-1]
        self.dy = [1,-1,0,0]
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j , grid):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 2
            res = 1
            for k in range(4):
                ii = i + self.dx[k]
                jj = j + self.dy[k]
                res += dfs(ii,jj,grid)
            return res
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i , j, grid))
        return maxArea
