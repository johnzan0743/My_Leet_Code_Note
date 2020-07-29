from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        n = len(grid)
        if grid[n-1][n-1] == 1:
            return -1 
        if n == 1:
            return 1
            # 此时grid只有一行，由于题中说grid是N*N，所以相当于只有一个格子，所以一步到位
        path = []
        result = 1
        path.append([0,0])
        while path:
            for i in range(len(path)): # 注意：一定要注意是对path队列内部进行循环！
                x,y = path.pop(0) # 先进先出
                for new_x, new_y in [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]:
                    if not 0 <= new_x < n or not 0 <= new_y < n: 
                        # out of boundary
                        continue
                    if grid[new_x][new_y] == 1: # blocked
                        continue
                    if grid[new_x][new_y] == -1: # visited
                        continue
                    if new_x == n - 1 and new_y == n - 1: 
                        # reach to the last element
                        return result + 1
                    if grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = -1
                        # could be grid[new_x][new_y] = 1
                        # 把visited和blocked都统一为1，反正都是不能再访问了
                        path.append([new_x,new_y])
            result +=1 
            # 对某一层的元素都求判定过后，距离加1(同一个层次中的所有点的距离距离起点都是相等的）
            # 这里的某一层是指BFS中的一层，而不是grid中的一层。BFS中的一层是指与起点距离相同的元素
        return -1