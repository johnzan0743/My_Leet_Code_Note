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

# Set法
class Solution:
    def frequencySort(self, s: str) -> str:
        str_set=set(s)
        count_list=[[i,s.count(i)] for i in str_set]
        count_list.sort(key=lambda x:x[1],reverse=True)
        sort_str=''
        for i in countlist:
            sort_str+=i[0]*i[1]
        return sort_str