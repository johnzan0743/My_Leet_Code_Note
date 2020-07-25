class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        p1 = 1
        p2 = n
        while p1 < p2:
            mid = (p1+p2)//2
            
            if isBadVersion(mid):
                p2 = mid
            else:
                p1 = mid + 1
        return p1