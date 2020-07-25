from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        check_board = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if check_board[i][j] is False:
                        count +=1
                        check_board[i][j] = True
                        queue = []
                        queue.append([i,j])
                        while queue:
                            temp = queue.pop(0)
                            p = temp[0]
                            q = temp[1]
                            if p + 1 <= len(grid)-1 and check_board[p+1][q] is False and grid[p+1][q] == '1':
                                queue.append([p+1,q])
                                check_board[p+1][q] = True
                            if p-1 >=0 and check_board[p-1][q] is False and grid[p-1][q] == '1':
                                queue.append([p-1,q])
                                check_board[p-1][q] = True
                            if q-1 >=0 and check_board[p][q-1] is False and grid[p][q-1] == '1':
                                queue.append([p,q-1])
                                check_board[p][q-1] = True
                            if q+1 <= len(grid[0])-1 and check_board[p][q-1] is False and grid[p][q+1] == 1:
                                queue.append([p,p+1])
                                check_board[p][q+1] = True

        return count
    


                                