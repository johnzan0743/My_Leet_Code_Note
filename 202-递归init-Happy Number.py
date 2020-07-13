class Solution:
    def __init__(self):
        self.flag = 0
    def isHappy(self, n: int) -> bool:
        if not n or n <= 0:
            return False
        else:
            seen = []
            total = 0
            self.squareSum(n,seen,total)
            return self.flag == 1
    def squareSum(self,n,seen,total):
        result = []
        
        while n > 0:
            temp = n%10
            result.append(temp)
            n = n//10
        for i in result:
            total += i**2
        if total == 1:
            self.flag = 1
            return self.flag
        elif total not in seen:
            seen.append(total)
            n = total
            total = 0
            self.squareSum(n,seen,total)
        else:
            self.flag = 2
            return self.flag

