class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.dx = [1,-1,0,0]
        self.dy = [0,0,1,-1]

        r = len(grid)
        c = len(grid[0])
        maxArea = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(i,j,grid))
        return maxArea
        
    def dfs(self,i,j,grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        
        grid[i][j] = 2
        area = 1
        for k in range(4):
            ii = i + self.dx[k]
            jj = j + self.dy[k]
            area += self.dfs(ii,jj,grid)
        return area