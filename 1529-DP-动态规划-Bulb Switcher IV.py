class Solution:
    def minFlips(self, target: str) -> int:
        dp = [0 for i in range(len(target))]
        if target[0] == '0':
            dp[0] = 0
        elif target[0] == '1':
            dp[0] = 1
        
        for i in range(1,len(target)):
            if target[i] == target[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
        return dp[-1]