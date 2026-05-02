class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i , j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
                return 
            
            grid[i][j] = '2'
            for r,c in directions:
                dfs(i + r, j + c)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i , j)
                    count += 1

        return count