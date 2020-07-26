from typing import List
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
            # 此处必须返回列表，因为列表是iterable 可迭代对象

        result = [] # result初始化
        operator  = ['+','*','-']

        for i in range(len(input)):
            if input[i] in operator:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for left_digit in left:
                    for right_digit in right:
                        if input[i] == '+':
                            result.append(left_digit + right_digit)
                        elif input[i] == '-':
                            result.append(left_digit - right_digit)
                        elif input[i] == '*':
                            result.append(left_digit * right_digit)
        return result