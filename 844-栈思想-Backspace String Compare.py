class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for i in S:
            if i != '#': 
                stack_s.append(i)
            elif stack_s:
                stack_s.pop()
        for i in T:
            if i != '#':
                stack_t.append(i)
            elif stack_t:
                stack_t.pop()
        return stack_s == stack_t
'''
此题使用栈的思想
当压入的是字母的时候就append
当遇到#的时候，就pop最后压入的字母
特例：当栈为空时，遇到#跳过，即只有当栈不为空时遇到#才弹出last element
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def new_list(string, answer):
            for i in string:
                if i == '#':
                    if answer:
                        answer.pop()
                else:
                    answer.append(i)
            return answer
        S_list = []
        T_list = []
        S_list = new_list(S,S_list)
        T_list = new_list(T,T_list)

        return S_list == T_list