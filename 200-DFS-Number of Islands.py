from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        for i in range(len(grid)):
            grid[i] = ['0']+grid[i]+['0']
        extra = ['0' for i in range(len(grid[0]))]
        grid.insert(0,extra)
        grid.insert(len(grid),extra) # 注意insert序号 若加到最后，序号为len（list）
        
        check_board = [[False for i in range(len(grid[0]))] for i in range(len(grid))] # check whether visted or not
        count = 0
        # m = len(grid)
        # n = len(grid[0])
        
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == '1':
                    if check_board[i][j] is False:
                        self.dfs(grid,i,j,check_board)
                        count +=1

        return count
                
        
    def dfs(self,candidates,i,j,check_board):  
        # potential m and n 
        # m = len(grid), n = len(grid[0])
        if check_board[i][j] is True:
            return 
        check_board[i][j] = True
        
        #if i > m-2 or i < 1 or j > n-2 or j < 1:
            #return
        

        if candidates[i][j] == '0':
            
            return
        

        self.dfs(candidates,i,j+1,check_board)
        self.dfs(candidates,i,j-1,check_board)
        self.dfs(candidates,i+1,j,check_board)
        self.dfs(candidates,i-1,j,check_board)