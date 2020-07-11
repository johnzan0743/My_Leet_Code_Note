class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ''
        if not strs:
            return ''
        i = 0
        while i < len(min(strs,key=len)):
            for string in strs:
                temp = strs[0][i]
                if string[i] != temp:
                    break
            if string[i] != temp:
                break
            else: 
                prefix +=temp
                i +=1
        return prefix