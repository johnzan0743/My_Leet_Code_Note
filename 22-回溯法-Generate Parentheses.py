class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        temp = ''
        left = ['('] * n
        right = [')'] * n
        def dfs(left, right, temp, result):
            if len(left) == len(right) == 0:
                result.append(temp)
                return
            if len(left) > 0:
                dfs(left[0:-1],right,temp+'(',result)
            if len(left) < len(right):
                dfs(left, right[0:-1], temp+')', result)
        dfs(left,right,temp,result)
        return result

# 更好的写法是直接写left = right = n  

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        temp = ''
        left = right = n
        self.dfs(left,right,temp,result)
        return result
    def dfs(self,left,right,temp,result):
        if left == right == 0:
            result.append(temp)
            return
        if left > 0:
            self.dfs(left-1,right,temp+'(',result)
        if left < right:
            self.dfs(left,right-1,temp+')',result)