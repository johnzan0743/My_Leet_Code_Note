class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        count = collections.Counter(s)
        # key是字符，value是出现次数
        new_key = sorted(count.keys(),key=count.get,reverse=True)
        # new_key的排序是按照values出现频率 从大到小排序
        res = ''
        for i in new_key:
            res += count[i]*i
        return res