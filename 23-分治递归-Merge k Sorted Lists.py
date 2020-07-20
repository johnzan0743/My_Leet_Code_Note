class Solution:
    def mergeKLists(self, lists):    
        if not lists:
            return None
        
        def helper(begin, end):
            if begin == end:
                return lists[begin]
            mid = begin + (end-begin)//2
            left = helper(begin,mid)
            right = helper(mid + 1,end) # 此处不理解
            # 不断递归，每递归一次，就二分法拆一次，直到只剩一个链表
            # 用两个最小单位的链表进行合并
            return merge(left,right)
        # 合并两个有序链表
        def merge(a,b):
            if not a:
                return b
            elif not b:
                return a
            else:
                if a.val < b.val:
                    a.next = merge(a.next,b)
                    return a
                else:
                    b.next = merge(a,b.next)
                    return b
        return helper(0,len(lists)-1)