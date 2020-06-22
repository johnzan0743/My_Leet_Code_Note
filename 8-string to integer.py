class Solution:
    def myAtoi(self, str: str) -> int:
        integer_set = {'0','1','2','3','4','5','6','7','8','9'}
        if str.isspace() or not str or str.strip() == '+' or str.strip() == '-':
            return 0
        elif str.strip()[0] == '+' or str.strip()[0] == '-':
            i = 1
            while i in range(len(str.strip())):
                if str.strip()[i] in integer_set:
                    i +=1
                elif str.strip()[1] not in integer_set:
                    return 0
                else:
                    break
        else:
            i = 0
            while i in range(len(str.strip())):
                if str.strip()[i] in integer_set:
                    i +=1
                elif str.strip()[0] not in integer_set:
                    return 0
                else:
                    break
        integer = str.strip()[0:i]
        integer = int(str.strip()[0:i])
        if integer >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif integer <= -2 ** 31:
            return -2 ** 31
        else:
            return integer