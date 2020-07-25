class Solution:
    def mySqrt(self, x: int) -> int:
        if not x or x == 0:
            return 0
        if x == 1:
            return 1
        p1 = 0
        p2 = x

        while p1 < p2:
            mid = (p1+p2)//2
            if mid * mid == x:
                return mid
            elif p2 - p1 == 1:
                return p1
            elif mid * mid < x:
                p1 = mid
            elif mid * mid > x:
                p2 = mid