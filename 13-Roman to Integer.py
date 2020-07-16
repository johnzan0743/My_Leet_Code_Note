class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        dict1 = {'I': 1, 'V': 5,'X': 10, 'L': 50, \
        'C':100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            if dict1[s[i]] >= dict1[s[i+1]]:
                result += dict1[s[i]]
            else:
                result -= dict1[s[i]]
        result +=dict1[s[-1]]
        return result