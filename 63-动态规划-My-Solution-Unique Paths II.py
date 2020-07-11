class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid)  # n是行数
        m = len(obstacleGrid[0]) # m是列数
        for i in range(m):
            for j in range(n):
                if obstacleGrid[j][i] == 1:
                    obstacleGrid[j][i] = -1
        for i in range(m):
            if obstacleGrid[0][i] == -1:
                #obstacleGrid[0][0:i] = [1]*i
                break
            else:
                obstacleGrid[0][i] = 1
        for i in range(n):
            if obstacleGrid[i][0] == -1:
                #obstacleGrid[0:i][0] = [1] * i
                break
            else:
                obstacleGrid[i][0] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == -1:
                    continue 
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    if obstacleGrid[i-1][j] == -1:
                        obstacleGrid[i][j] +=1
                    if obstacleGrid[i][j-1] == -1:
                        obstacleGrid[i][j] +=1
        if obstacleGrid[-1][-1] == -1:
            obstacleGrid[-1][-1] = 0
        return obstacleGrid[-1][-1]