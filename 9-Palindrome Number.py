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