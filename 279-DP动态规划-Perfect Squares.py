class Solution:
    def numSquares(self, n: int) -> int:
        f = [float('inf') for i in range(n+1)]
        f[0] = 0
        f[1] = 1
        # f[n]表示的状态是，当正整数为n时，组成n的最少平方数的个数
        for i in range(2,n+1):
            for j in range(1,i):
                if j*j <=i:
                    f[i] = min(f[i],f[i-j*j]+1)
                else:
                    break
        return f[n]