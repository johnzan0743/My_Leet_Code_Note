# 300-DP动态规划-Longest Increasing Subsequence
# 子串substring 一定是要连续的
# 子序列subsequence 不一定是连续的
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1 for i in range(len(nums))]
        # dp中的每个元素至少为1
        # dp[i]表示的是以第i个元素为结尾的最长的升序子序列


        result = 1  # 为了防止nums中所有元素都一样大，无法进入下面的大小判断

        for i in range(nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                    # 只要nums[i]>nums[j]，dp[i]就天然要比dp[j]多一个
                    # 由于dp[i]会被dp[j]多次赋值，所以要取max
                    result = max(result,dp[i])
        return result