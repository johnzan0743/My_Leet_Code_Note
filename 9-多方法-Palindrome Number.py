# String 法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            flag = True
            x = str(x)
            for i in range(len(x)):
                if x[i] != x[-1-i]:
                    flag = False
                    
            return flag
# 列表法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if not x:
            return False

        
        if x < 0:
            return False
        number = []
        while x > 0:
            digit = x % 10
            number.append(digit)
            x = x//10
        return number == number[::-1]


# 数字翻转法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if not x:
            return False
        if x < 0:
            return False
        result = 0
        origin_x = x
        while x > 0:
            digit = x %10
            x = x //10
            result = result * 10 + digit
        return result == origin_x