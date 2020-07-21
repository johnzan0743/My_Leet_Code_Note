class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        #if len(cost) <= 2:
            #return min(cost[0],cost[1])
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[0],cost[1])
        dp = {}
        dp[0] = 0
        dp[1] = min(cost[0],cost[1])
        dp[2] = min(dp[0]+cost[1],dp[1]+cost[2])
        # dp[3] = min(dp[2]+cost[3],dp[1]+cost[2])
        # dp[4] = min(dp[3]+cost[4],dp[2]+cost[3])
        # dp[i] 表示的是如果楼顶在第i层上面，所需要的最低花费
        for i in range(3,len(cost)):
            dp[i] = min(cost[i]+dp[i-1], cost[i-1]+dp[i-2])
        return dp[len(cost)-1]