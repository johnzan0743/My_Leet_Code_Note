class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        dp = [1 for i in range(len(points))]
        result = 1
        points.sort(key=lambda x:x[1])

        for i in range(len(points)):
            for j in range(i-1,-1,-1):
                if points[i][0] > points[j][1]:
                    dp[i] = dp[j] + 1
                    break
            dp[i] = max(dp[i],dp[i-1])
            result = max(result, dp[i])
        return result