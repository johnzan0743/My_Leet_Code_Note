class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # from math import sqrt
        first = 0
        second = int(c **0.5)
        # second = int(sqrt(c))
        while first <= second:
            if first **2 + second **2 > c:
                second -=1
            elif first **2 + second **2 < c:
                first +=1
            elif first **2 + second **2 == c:
                return True
        return False