class Solution:
    def isValid(self, s: str) -> bool:
        dic1 = {'(':')','[':']','{':'}'}
        stack = []
        for item in s:
            if item in dic1.keys():
                stack.append(item)
            elif len(stack) == 0 or item != dic1[stack.pop()]: 
                #either左括号用完了或者括号类型对不上
                return False
        if len(stack) == 0: 
            return True
        else:   #'['
            return False