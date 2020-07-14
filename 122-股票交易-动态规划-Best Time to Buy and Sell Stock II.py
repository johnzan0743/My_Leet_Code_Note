class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices or len(prices) == 1:
            return profit
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit +=prices[i] - prices[i-1]
        return profit
# 此题的核心是抓住每一个单调递增曲线
# 由于可以无限买卖
# 所以最大获益就等于每一段上扬曲线（单调递增）累加
# 连续下降交易日： 则不买卖收益最大，即不会亏钱。
# 上面的这种算是贪心算法，因为只是考虑局部最优解
# 而下面则是动态规划，其实贪心算法算是一种有限的动态规划

'''
DP为一个二维数组，分别代表天数i和是持有股票（1）还是持有现金（0）,赋值为最大获利数值

DP[i][0]: 第i天手里没有股票，分两种情况:
要么是第i-1天手里就没有股票，第i天也没买股票
要么是第i-1天手里有股票，第i天卖出股票

DP[i][1]：第i天手里持有股票，分两种情况:
要么是第i-1天手里就持有股票，第i天继续持有股票，没有卖出
要么是第i-1天手里没有股票，第i天买入股票

所以状态转移方程就是：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][1] - price[i])

DP状态初始化：
dp[0][0] = 0 第一天没有股票，说明没买没卖，获利为0
dp[0][1] = -price[0] 第一天持有股票，说明买入了，花掉一笔钱

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]    # 返回最后一天且手上没有股票时的获利情况

