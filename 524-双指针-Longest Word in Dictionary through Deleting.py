class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 首先对列表d排序，第一优先是长度，由长到短；第二优先是字典序
        d = sorted(d,key =lambda x:(-len(x),x))
        # lambda函数 输入x，输出第一优先x的长度（倒序），第二优先x字母顺序

        for word in d:
            index = 0
            for i in range(len(s)):
                if s[i] == word[index]: # 因为可以对s中的字符进行任意删减，所以只需要考虑是否在排序上与列表d中的单词一致就可以了
                    index +=1
                if index == len(word): # 注意是index 而不是index + 1
                    return word
                # 由于已经对列表d里面的word进行了长度排序和字典序排序，所以第一个完整匹配的word就是最优解
        return ''
        