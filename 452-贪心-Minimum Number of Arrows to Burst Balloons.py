# 参考435题 贪心
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0
        points.sort(key = lambda x:x[1])

        end = -float('inf')
        count = 0

        for point in points:
            start = point[0]
            if start > end:
                count +=1
                end = point[1]
        
        return count