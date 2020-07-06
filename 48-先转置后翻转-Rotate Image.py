class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for rows in matrix:
            rows.reverse()
'''            
原matrix
1, 2, 3, 4, 5
6, 7, 8, 9, 10
11,12,13,14,15
16,17,18,19,20
21,22,23,24,25

转置matrix 沿对称线转置，即需要有条件i<j 或i>j 来避免重复翻转
1,6, 11,16,21
2,7, 12,17,22
3,8, 13,18,23
4,9, 14,19,24 
5,10,15,20,25

左右翻转matrix
21，16，11，6， 1
22，17，12，7， 2
23，18，13，8， 3
24，19，14，9， 4
25，20，15，10，5
'''