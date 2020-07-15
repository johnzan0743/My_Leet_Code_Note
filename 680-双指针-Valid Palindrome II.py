class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return False
        if len(s) == 1 or len(s) == 2:
            return True
        if s == s[::-1]:
            return True
        left = 0
        right = len(s) -1
        #此时字符串s一定需要删除一个元素，才有可能达成回文要求
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            if s[left] != s[right]:
                break
        aa = s[left+1:right+1] == s[right:left:-1]
        # 把左指针位置字符删除，前进一位

        # 下面是删除右指针的情况，小心边界问题
        if left == 0:  # 小心超越边界的情况
            bb = s[left:right] == s[right-1::-1]
        else:
            bb = s[left:right] == s[right-1:left-1:-1]
        return aa or bb