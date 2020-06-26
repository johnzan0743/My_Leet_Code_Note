class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ''
        if not strs:
            return ''
        
        
        i = 0
        temp_set = set()
        while i < len(min(strs,key=len)):
            for string in strs:
                temp_set.add(string[i])
                if len(temp_set) > 1:
                    break
            if len(temp_set) > 1:
                break
            else:
                prefix +=strs[0][i]
                temp_set.pop()
                i +=1
        return prefix