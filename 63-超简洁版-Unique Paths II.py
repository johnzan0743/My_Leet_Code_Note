class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [1] + [0]*m
        for i in range(0, n):
            for j in range(0, m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-1]

A = Solution()
obstacleGrid = [[0,0,0],[1,1,0],[0,0,0]]
B = A.uniquePathsWithObstacles(obstacleGrid)

'''
dp为当前需要操作的array，即一个条状的strip
给整个obstacleGrid的最左边加一个全0列
这在dp上体现为在最右边加一个0
这样对于第一列来说，所有的dp[0]就只能从上一行继承而来
如果上一行的dp[0]=0 或者本行的的dp[0] = 0， 则下面所有行的dp[0]都为0

dp[0]默认为1，一旦有一行（也可能是第一行）的obstacleGrid的第0个元素为1（即存在障碍物），则dp[j] = 0， 之后也彻底为0
在没有障碍物存在的情况下， dp[j] = dp[j] + dp[j-1] 这句话的意思是
第一个dp[j]为本行要赋值的元素
第二个dp[j]为上一个行的dp[j]
dp[j-1]为本行第j个元素的前一个（左边）元素
'''