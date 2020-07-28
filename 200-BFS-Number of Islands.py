from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        path = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    grid[row][col] = '-1' # 别忘了改状态 防止重复visit
                    path.append([row,col])
                    while path:
                        x,y = path.pop(0)
                        for new_x,new_y in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                path.append([new_x,new_y])
                                grid[new_x][new_y] = '-1' 
        return count