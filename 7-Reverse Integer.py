class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x >= 0:
            x_reverse = x_str[::-1]
        else:
            temp = x_str[::-1]
            x_reverse = '-' + temp[0:-1]
        if int(x_reverse) <= 2 ** 31 -1  and int(x_reverse) >= -2 ** 31:
            return int(x_reverse)
        else:
            return 0