from typing import List

# 这个题用贪心的原因是，题目问删掉最少的空间使得剩余空间不严格递增
# 大概的意思就是尽量让剩余空间尽量紧凑
# 最极致的情况就是一直连续而不用删除：[1,2],[2,3],[3,4]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x:x[1])

        end = -float('inf')
        count = 0
        for interval in intervals:
            start = interval[0] # 区间下限（最小值）
            # 每次循环都会有新的interval start出现，interval end不变
            # 直到找到刚好比上一个区间的上限更大的interval的上限
            if start >= end:
                count +=1
                end = interval[1] #同一区间的上限（最大值）
            #else:
                #continue
        return len(intervals) - count