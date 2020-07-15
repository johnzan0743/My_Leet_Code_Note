class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 2:
            return True
        left = 0
        right = len(s) -1
        if s == s[::-1]: # 先判断原字符串是否本身就是回文
            return True
        else:
            if len(s)%2 == 1: 
                # abcba 原字符串是奇数长度 删除一个字符后变成偶数长度
                # 即删除之后 为abba类型
                count = 0
                while left < right:
                    if s[left] == s[right]:
                        left +=1
                        right -=1
                    elif left + 1 < right and s[left+1] == s[right]:
                        left +=1
                        count +=1
                        if count > 1:
                            return False
                    elif left < right -1 and s[left] == s[right-1]:
                        right -=1
                        count +=1
                        if count > 1:
                            return False
                    else: return False
                return True
            elif len(s)%2 == 0:
                #在排除了本身是回文的基础上
                #原来是偶数的字符串，现在必须删掉一个变成奇数型回文
                #abcba
                count =0
                while left < right:
                    if s[left] == s[right]:
                        left +=1
                        right -=1
                    '''
                    elif left+1 < right and s[left+1] == s[right]:
                        left +=1
                        count +=1
                        if count > 1:
                            return False
                    elif left < right -1 and s[left] == s[right-1]:
                        right -=1
                        count +=1
                        if count > 1:
                            return False
                    经验教训：自己想太多，以后回文直接按照定义，交给计算机自己算，不要自作聪明
                    有一种特殊情况就是我在某个节点，删除左边的元素和删除右边的元素都可以暂时达成回文，但是剩下的字符串中，只有一种情况可以达成回文，这个非常坑
                    '''
                    elif left +1 == right and count == 0:
                        return True
                    else: return False
                return True
