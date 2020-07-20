class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1 # 这一句只有当l1和l2同时有同样的长度，一起跑完之后比较最后一个节点的时候，才会被执行到
            else:
                l2.next = self.mergeTwoLists(l1,l2.next)
                return l2
# 整个递归的逻辑是如果l1.val比l2.val小，那么我们就以l1为起点
# l1.next是比较l1.next和l2的结果
# 同理如果l2比l1小，那么我们就以l2为起点
# l2.next是比较l2.next和l1的结果