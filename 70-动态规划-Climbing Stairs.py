class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 由于最后一阶可以视为由倒数第一阶或倒数第二阶跳上来的
        # 所以dp[n]储存跳到第n阶的可能方法
        # 则 dp[n] = dp[n-1] + dp[n-2]
        if n > 2:
            dp = {}
            dp[1] = 1
            dp[2] = 2
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]