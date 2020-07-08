class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(m)] for i in range(n)]
        # n represents the number of rows
        # m represents the number of columns
        # the value of the cell represents the total number of ways from start to move to the cell.
        # dp transition function:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(m):
            matrix[0][i] = 1
        for i in range(n):
            matrix[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
        return matrix[n-1][m-1]  # matrix[-1][-1]