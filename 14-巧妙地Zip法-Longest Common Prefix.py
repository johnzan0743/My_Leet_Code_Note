class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        strings = zip(*strs)
        # strs = ["flower","flow","flight"]
        # list(strings) = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        for i in strings:
            temp_set = set(i)
            if len(temp_set) == 1:
                result +=i[0] 
                #i是元组tuple，有index，而temp_set是集合set，没有index
            else:
                break
        return result