# Michelle Version
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

#My Own Version
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dic1 = {'(':')','[':']','{':'}'}
        stack = []
        for item in s:
            if item in dic1.keys():
                stack.append(item)   #把所有左括号加入stack中
            else:
                if len(stack) > 0 and item == dic1[stack[-1]]:
                    stack.pop()   #如果找到右括号，而且此时stack中还有对应的左括号，则pop左括号
                else:  #如果左括号stack为空，则说明左括号已经用完，则是False
                    return False
        if len(stack) == 0:
            return True