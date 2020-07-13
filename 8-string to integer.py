class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        str = str.strip()
        if not str:
            return 0
        A = ('0','1','2','3','4','5','6','7','8','9')
        result = ''
        if str[0] not in A:
            if str[0] == '+' or str[0] == '-':
                for i in range(1,len(str)):
                    if str[i] in A:
                        result += str[i]
                    else:
                        break
                result = str[0] + result
                if len(result) == 1: # when only + or - exists
                    return 0
            else:
                return 0
        else:
            for i in range(len(str)):
                if str[i] in A:
                    result += str[i]
                else:
                    break
        if result[0] == '+':
            if int(result[1:]) > 2**31 - 1:
                return 2 ** 31 -1
            else: return int(result[1:])
        elif result[0] == '-':
            if int(result) < -2**31:
                return -2 ** 31
            else: return int(result)
        else: 
            if -2**31 <= int(result) <= 2**31 -1:
                return int(result)
            elif int(result) > 2 **31 -1:
                return 2**31 -1
            elif int(result) < -2 **31:
                return -2**31