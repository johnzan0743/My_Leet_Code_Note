class Solution:
    def longestValidParentheses(self,s):
        if not s:
            return 0
        stack = [-1]   # stack中记录的是序号索引index
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # 如果空栈，立即把当前序列作为参考物入栈
                    stack.append(i)
                else:
                    result = max(result,i-stack[-1])
                    # '(()' 此处必须是i-stack[-1] 而不是i-stack[0]
                    # 当然极限情况，就是所有的左括号全部匹配完毕，则通过之前的右括号所做的参照物来计算长度，此时 i - stack[-1] == i - stack[0]
        return result