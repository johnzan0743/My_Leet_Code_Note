class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j] = 0
'''
此题时间复杂度为O(M X N)
额外空间复杂度为O(M + N)  需要多余的两个set分别记录需要变为0的矩阵行序列和矩阵列序列
'''