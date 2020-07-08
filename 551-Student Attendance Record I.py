class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count_A +=1
                if count_A == 2:
                    return False
            if s[i] == 'L':
                count_L +=1
                if count_L == 3:
                    return False
            else:  #如果当前字符不是L，则连续迟到次数清零
                count_L = 0
        return True
