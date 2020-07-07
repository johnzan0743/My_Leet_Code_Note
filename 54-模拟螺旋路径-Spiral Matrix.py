class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return list()
        m = len(matrix) # m represents the number of rows
        n = len(matrix[0]) # n represents the number of columns
        result_matrix = [0 for i in range(n*m)]
        if m == 1:
            return matrix[0]
        visited = [[False for i in range(n)] for i in range(m)]
        x = y = 0  # x,y coordinates
        right = [0, 1]
        left = [0, -1]
        up = [-1, 0]
        down = [1, 0]
        direction_list = [right,down,left,up]
        index = 0
        for i in range(n*m):
            result_matrix[i] = matrix[x][y]
            visited[x][y] = True
            '''
            if index%4 == 1:
                direction = right
            elif index%4 ==2:
                direction = down
            elif index%4 == 3:
                direction = left
            elif index%4 == 0:
                direction = up
            '''
            direction = direction_list[index%4]
            nx,ny = x+direction[0],y+direction[1]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False:
                x, y = nx, ny
            else:
                index +=1
                direction = direction_list[index%4]
                x,y = x+direction[0],y+direction[1]
        return result_matrix