class Solution:
    def letterCombinations(self, digits):
        digit = ['1','2','3','4','5','6','7','8','9']
        string = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        dic1 = dict(zip(digit,string))
        result = []
        path = ''
        if not digits:
            return []

        def dfs(digits,path):
            if not digits:
                result.append(path)
                return
            
            for letter in dic1[digits[0]]:
                dfs(digits[1:],path+letter)
            # 原理是我们从digits[0]所有的value中拿出一个letter，加入path
            # 再重新定义candidates的空间，在新的digits[0]所有value中拿出一个letter加入path
            # 注意返回的时候也是顺次返回，先把最后一层（即digits[-1]所代表的所有letter全部添加完毕，再遍历digits[-2]中第二个letter
        dfs(digits,path)
        return result


