class Solution:
    def maxProfit(self, prices):
        minprice = float('inf') 
        # 或 minprice = prices[0], 但是前面需要有判断条件：if len(prices) > 0:
        maxprofit = 0
        for price in prices:
            minprice = min(price, minprice)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit
# 此题的核心思路是一次性交易获取最大收益，即只能买卖一次
# 所以必须要先买入再卖出
# 我们的思路是每次股价变化都尝试买入，这样取得最低买入价
# 随后用当日的股价减去历史最低股价，获取当日最大利润
# 并与历史最大利润比较，从而获取历史最大利润
# 上面是一般方法
# 不过更建议使用下面的动态规划法

class Solution():
    def maxProfit(self,prices):
        if len(prices) == 0:
            return 0
        dp = [0 for i in range(len(prices))]

        minprice = prices[0]

        for i in range(1,len(prices)):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)
        return dp[-1]
# 此题由于只有一次交易，所以相比较第122题，少了股票持有状态的判断
# dp[i]的赋值等于从**minprice最低买入价那一天开始算**，第i天卖出的话，最大的收益是多少。
# 注意：只有在最低买入价以后的最高卖出价是有意义的，因为必须要先买入再卖出，在最低买入价以前的最高卖出价都没有意义
# 如果第i天卖出，那么收益就是 prices[i]-minprice，这时候拿此数值跟dp[i-1]做大小比较，并取较大值赋值给dp[i]
# 如果dp[i-1]更大，那么就把dp[i-1]赋值给dp[i]，相当于第i-1天已经把股票卖掉了，并无法继续买入（因为只能买卖一次）
# 如果在第i天卖出获得的收益比第i-1天高，那么dp[i]就赋值 prices[i]-minprice，相当于股票从最低买入点开始，持续持有到第i天并于第i天卖出所获得的收益更高。
# 最后返回dp[-1]，即到最后一天，最大的收益的情况
 