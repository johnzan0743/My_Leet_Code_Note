class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [-float('inf') for i in range(len(nums))]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(dp[i],result)
        return result