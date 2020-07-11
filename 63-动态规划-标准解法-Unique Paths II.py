class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                temp[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                temp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]

作者：LotusPanda
链接：https://leetcode-cn.com/problems/unique-paths-ii/solution/xiong-mao-shua-ti-python3-2wei-dpzhu-yi-bi-kai-pyt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。