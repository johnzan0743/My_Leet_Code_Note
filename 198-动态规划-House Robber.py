class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) > 2:
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i]) 
                # 偷第i-1家的代价是不能偷第i-2家和第i家，所以要权衡两者的大小
            return dp[-1]