def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {'2':"abc",
             '3':"def",
             '4':"ghi",
             '5':"jkl",
             '6':"mno",
             '7':"pqrs",
             '8':"tuv",
             '9':"wxyz"
            }
        res = []
        self.dfs(d, digits, "", res)
        return res
    
    def dfs(self, d, digits, tmp , res):
        if not digits:
            res.append(tmp)
        else:
            for num in d[digits[0]]:
                self.dfs(d, digits[1:], tmp + num, res)
