class Solution:
    def letterCombinations(self, digits: str):
        key = ['0','1','2','3','4','5','6','7','8','9']
        value = ['', '', 'abc','def','ghi','jkl','mno','pqrs',\
                 'tuv','wxyz']
        mapping = dict(zip(key,value))
        if not digits:
            return []
        
        result_list = [''] # 注意，此处必须这么写
        for digit in digits:
            temp_list = []
            digit_characters = mapping[digit]
            for character in digit_characters:
                for item in result_list:
                    temp_list.append(item + character)
            result_list = temp_list
            
        return result_list
    

digits = "23"
A = Solution()
B = A.letterCombinations(digits)