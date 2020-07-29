class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        if all(row.count(1) == 0 for row in grid):
            return 0
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = 0
                    grid[row][col] = 0
                    queue = []
                    queue.append([row,col])
                    while queue:
                        x,y = queue.pop(0)
                        for new_x,new_y in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                                queue.append([new_x,new_y])
                                grid[new_x][new_y] = 0
                        count +=1
                    result = max(result,count)
        return result