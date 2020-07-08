class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if matrix[0] == []:
            return False

        n = len(matrix)
        m = len(matrix[0])
        # n 行 m 列
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        else:
            low = 0
            high = n-1
            while high >= low: #考虑万一只有一行的情况
                mid = (high+low)//2
                if target == matrix[mid][0]:
                    return True
                if target > matrix[mid][0]:
                    if target <= matrix[mid][-1]:
                        #target比mid行第一位大，比mid行最后一位小
                        #此时在mid这一行里寻找
                        left = 0
                        right = m-1
                        while right >= left:
                            middle = (left+right)//2
                            if target == matrix[mid][middle]:
                                return True
                            if target > matrix[mid][middle]:
                                left = middle + 1
                            if target < matrix[mid][middle]:
                                right = middle - 1
                        #如果整行用二分法查找之后都找不到target的话，说明target不存在
                        return False
                    else:
                        low = mid + 1
                if target < matrix[mid][0]: 
                    if target > matrix[mid-1][-1]:
                        #比上一行最大的数大但是比mid行最小的数小
                        return False
                    else:
                        high = mid - 1

2020-07-08-18-48-10.png