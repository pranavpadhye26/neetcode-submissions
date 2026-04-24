class Solution:
    def __init__(self):
        # self.dx=[1,-1,0,0]
        # self.dy=[0,0,1,-1]
        self.dx = [1,-1,0,0]
        self.dy = [0,0,1,-1]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.r = len(grid)
        self.c = len(grid[0])
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    count += 1
        return count

    def dfs(self,i,j,grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '2'
        for k in range(4):
            ii = i + self.dx[k]
            jj = j + self.dy[k]
            self.dfs(ii,jj,grid)
        # ifi<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
        #     return
        
        # grid[i][j]='2'
        # for k in range(4):
        #     ii = i + self.dx[k]
        #     jj = j + self.dy[k]
        #     self.dfs(ii,jj,grid)