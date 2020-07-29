from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        
        if not grid:
            return 0
        if all(row.count(1)==0 for row in grid):
            return 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.count = 0
                    self.count = self.dfs(row,col,grid)
                    result = max(result,self.count)
        return result

    
    def dfs(self,x,y,grid):
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            return 
        
        if grid[x][y] == 0:
            return 
        elif grid[x][y] == 1:
            grid[x][y] = 0 # visited
            #count +=1
            self.count +=1
        


        self.dfs(x+1,y,grid)
        self.dfs(x-1,y,grid)
        self.dfs(x,y-1,grid)
        self.dfs(x,y+1,grid)
        return self.count