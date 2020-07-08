class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m 列 n 行
        # dp[i][j] = min(grid[i][j] + dp[i-1][j],grid[i][j] + dp[i][j-1])
        m, n = len(grid[0]), len(grid)
        sum_grid = [[0 for i in range(m)] for i in range(n)]
        sum_grid[0][0] = grid[0][0]
        for i in range(1,m):
            sum_grid[0][i] = sum_grid[0][i-1] + grid[0][i]
        for i in range(1,n):
            sum_grid[i][0] = sum_grid[i-1][0] + grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                sum_grid[i][j] = min(grid[i][j] + sum_grid[i-1][j], grid[i][j] + sum_grid[i][j-1])
        return sum_grid[-1][-1]