class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        import heapq
        count = collections.Counter(nums)
        ans = heapq.nlargest(k,count.keys(), key = count.get)
        # 上述语句的意思是，对于count这个字典而言，通过heapq来取得最大的k个值
        # k是前k个最大的元素，而且取值的对应范围是nums中所有的元素
        # 排序关键词是count字典中的values大小顺序
        return ans
