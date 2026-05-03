class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        def dfs(i , j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            
            board[i][j] = 'S'
            for k in range(4):
                ii = i + dx[k]
                jj = j + dy[k]
                dfs(ii,jj)

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'