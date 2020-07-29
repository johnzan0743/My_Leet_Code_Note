from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        if not grid:
            return 0
        if all(row.count(1) == 0 for row in grid):
            return 0


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = 0
                    count = self.dfs(row,col,grid)
                    result = max(result,count)
        return result
    
    def dfs(self,x,y,grid):
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            return 0
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0 # 如果grid[x][y]不是0，则置0

        top = self.dfs(x-1,y,grid)
        bottom = self.dfs(x+1,y,grid)
        left = self.dfs(x,y-1,grid)
        right = self.dfs(x,y+1,grid)
        
        return 1 + top+bottom+left+right

        
        
        
