class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) == 1:
            return s
        for i in range(len(s)-1):
            A = self.findpalindromic1(s,i)
            B = self.findpalindromic2(s,i)
            result = max(result, A, B, key=len)
        return result

    
    
    def findpalindromic1(self,s, i, l=0, r=1):
        # abba
        while i+l >= 0 and i+r < len(s) and s[i+l] == s[i+r]:
            l -=1
            r +=1
        return s[i+l+1:i+r]
    def findpalindromic2(self, s, i, l = 0, r = 0 ):  
        # bbacc
        while i+r < len(s) and i+l >= 0 and s[i+l] == s[i+r]:
            l -=1
            r +=1
        return s[i+l+1:i+r]
        