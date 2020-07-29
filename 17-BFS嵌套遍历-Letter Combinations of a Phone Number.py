class Solution:
    def letterCombinations(self, digits: str):
        key = ['0','1','2','3','4','5','6','7','8','9']
        value = ['', '', 'abc','def','ghi','jkl','mno','pqrs',\
                 'tuv','wxyz']
        dic1 = dict(zip(key,value))
        if not digits:
            return []
        
        result = [''] # 注意，此处必须这么写
        for digit in digits:
            temp = []
            for char in dic1[digit]:
                for strings in result:
                    temp.append(strings + char)
            result = temp
        return result
    

digits = "23"
A = Solution()
B = A.letterCombinations(digits)