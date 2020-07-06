class Solution:
    def longestPalindrome(self, s: str) -> str:
        import copy
        s = list(s)
        s_reverse = s[::-1]
        row = []
        for i in range(len(s)+2):
            row.append(copy.deepcopy(0))
     
        matrix = []
        for i in range(len(s)+2):
            matrix.append(copy.deepcopy(row))
        p = 0
        mmax = 0

        matrix[0][2:2+len(s)] = s   
        #matrix[1:][0] = s_reverse
        for i in range(2,len(s)+2):
            matrix[i][0] = s_reverse[i-2]
        
        for i in range(2,len(s)+2):
            for j in range(2,len(s)+2):
                if matrix[i][0] == matrix[0][j]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    if matrix[i][j] > mmax:
                        mmax = matrix[i][j]
                        p, q = i ,j
        x = q-mmax-1

        return ''.join(s[x:x+mmax])

A=Solution()
#s='cbbbd'
#s='babad'
#s='abb'
#s= 'aacdecaa'
s='abcdbbfcba'
B = A.longestPalindrome(s)