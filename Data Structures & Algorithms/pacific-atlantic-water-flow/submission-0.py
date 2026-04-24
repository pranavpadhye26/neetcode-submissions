class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pfc,atl=set(),set()
        rows=len(heights)
        cols=len(heights[0])
        self.dx=[1,-1,0,0]
        self.dy=[0,0,1,-1]

        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))
            for k in range(4):
                rr = r + self.dx[k]
                cc = c + self.dy[k]
                dfs(rr,cc,visit,heights[r][c])
            
        for c in range(cols):
            dfs(0,c,pfc,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pfc,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pfc:
                    res.append([r,c])
        return res

