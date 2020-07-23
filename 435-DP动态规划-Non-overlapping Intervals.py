from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 这道题问我们删除最少数量的空间，使剩余的空间不重叠 
        # 这个题目用动态规划的思路是找到最长的不连续（也可以连续）上升子序列
        # 即删除之后，整个序列所有的元素都大于等于上一个元素

        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[1]) # 按照intervals[1]即上限排序

        dp = [1 for i in range(len(intervals))]
        result = 1
        for i in range(len(intervals)):
            for j in range(i-1,-1,-1):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i],dp[j]+1)
                    break
            dp[i] = max(dp[i],dp[i-1])
            result = max(result,dp[i])
            # 上面的一小段基本上相当于第300题的正着找
            # 但是前提是需要sort，300题本身没有排序，所以不能倒着找
            # 这个题之所以可以倒着找，是因为本身intervals已经根据区间上限进行了sort
            # 类似于
        '''
        for i in range(len(intervals)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
                    result = max(dp[i],result)
        '''
            
        return len(intervals) - result