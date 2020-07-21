class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        elif numRows == 1:
            return s
        else:
            result = ['' for _ in range(numRows)]
            row = 0
            for i in range(len(s)):
                result[row] +=s[i]
                if row == 0:
                    flag = 1
                elif row == numRows-1:
                    flag = -1
                    
                row +=flag
            return ''.join(result), result
            

# 更工整的解法
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows >= len(s):
            return s
        if numRows == 1:
            return s
        result = ['' for _ in range(numRows)]
        final = ''
        p1 = 0

        for i in range(len(s)):
            if p1 == 0:
                flag = 1
            if p1 == numRows -1:
                flag = 0    
            
            
            if flag == 1:
                result[p1] +=s[i]
                p1 +=1
            if flag == 0:
                result[p1] +=s[i]
                p1 -=1
        for i in range(numRows):
            final +=result[i]
        return final