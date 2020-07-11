class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if strs == ['']:
            return ''
        # result = ''
        dict1 = {}
        # strs = sorted(strs,key=len)
        # s = min(strs,key=len)
        # s = min(strs, key = lambda string: len(string))
        strs = sorted(strs,key = lambda string: len(string))
        for i in range(len(strs[0])):
            dict1[i] = strs[0][i]
            for string in strs[1:]:
                if string[i] != dict1[i]:
                    return strs[0][0:i]
        return strs[0] #如果全部字符都相等，则返回strs[0]整体

