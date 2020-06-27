class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x >= 0:
            flag = 1
        else:
            flag = -1
        x = abs(x)
        while x > 0:
            digit = x % 10
            x = x // 10
            result = result * 10 + digit
        result = result * flag
        if result > 2**31 -1 or result < -2**31:
            return 0
        else: return result
