from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[-1 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        # new_matrix全部初始化为-1，这样可以有效判断是否visited
        # 正常情况下，原matrix上为0的点，新matrix也直接被赋予0
        # 并从这些0点向四周BFS寻找为-1的点
        # 找到后根据原点加1，并同时把新拓展的点加入队列
        path = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    new_matrix[row][col] = 0
                    path.append([row,col])
                    # 这个题的BFS考的是对于每一个0来说，如何通过BFS找到最近的1，找到后就把最近的距离赋值给那个新格子
        
        # 维护一个path队列，path中先进先出的是原matrix中所有为0的点，后入后出的是后来加入的原matrix中为1，新matrix中为-1的点
        while path:
            x, y = path.pop(0)
            for new_x,new_y in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and new_matrix[new_x][new_y] == -1:
                    new_matrix[new_x][new_y] = new_matrix[x][y] + 1
                    path.append([new_x,new_y])
        return new_matrix
        