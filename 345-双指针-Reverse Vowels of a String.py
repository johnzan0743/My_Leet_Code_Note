class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ''
        if len(s) == 1:
            return s
        s = list(s)
        set1 = {'a','e','i','o','u','A','E','I','O','U'}
        low = 0
        high = len(s) -1
        while low < high:
            if s[low] in set1 and s[high] in set1:
                s[low], s[high] = s[high], s[low]
                # 交换完成之后不要忘记移动指针，寻找下一组可能的组合
                low +=1
                high -=1
            elif s[low] in set1 and s[high] not in set1:
                high -=1
            elif s[low] not in set1 and s[high] in set1:
                low +=1
            else:
                low +=1
                high -=1
        return ''.join(s)