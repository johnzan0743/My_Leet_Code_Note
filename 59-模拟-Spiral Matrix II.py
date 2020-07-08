class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        #题目的意思是给一个正整数n 生成一个n*n的matrix，
        #并让所有数字从1到n**2顺时针螺旋排列
        matrix = [[0 for i in range(n)] for j in range(n)]
        visited = [[False for i in range(n)] for i in range(n)]
        right = [0,1]
        down = [1,0]
        left = [0,-1]
        up = [-1,0]
        direction_list = [right,down,left,up]
        index = 0
        x = 0
        y = 0
        for i in range(1,n**2+1):
            matrix[x][y] = i
            visited[x][y] = True
            nx,ny = x+direction_list[index%4][0], y + direction_list[index%4][1]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == False:
                x, y = nx, ny
            else:
                index +=1
                x, y = x+direction_list[index%4][0], y + direction_list[index%4][1]
        return matrix
