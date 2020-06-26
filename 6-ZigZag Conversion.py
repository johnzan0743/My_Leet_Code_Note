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
            



A=Solution()
s = "PAYPALISHIRING"
numRows = 3
B, C = A.convert(s,numRows)