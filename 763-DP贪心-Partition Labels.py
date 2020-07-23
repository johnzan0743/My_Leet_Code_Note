from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        if len(S) == 1:
            return [1]
        
        dic1 = dict()  #亦或是 dic1 = {}
        for i in range(len(S)):
            dic1[S[i]] = i   # 记录字母出现的最后位置
        result = []
        current = dic1[S[0]]  # current指针指的是字符串S中第一个元素出现的最后位置
        for i in range(len(S)):
            if dic1[S[i]] > current:
                current = dic1[S[i]] # 更新current的指针位置
            if i == current:
                result.append(current+1 - sum(result)) 
                # result存储的是每段字符串的长度
        return result