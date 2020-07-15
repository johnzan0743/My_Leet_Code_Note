class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        true_s = ''
        for i in s:
            if i.isalpha():
                true_s +=i.upper() # 记得要统一大小写
            elif i.isdigit():
                true_s +=i
        return true_s == true_s[::-1]