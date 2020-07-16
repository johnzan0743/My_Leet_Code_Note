# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        # 如果有环，那就一定会出现两者相遇的情况
        slow = fast = head
        while slow and fast.next: 
        # 这里更应该写成：
        # while fast and fast.next:
        # 这样可以避免下面的if not fast的判断 而且主要是需要判断fast和fast.next是否存在
        # 因为fast指针是开路先锋，只要fast指针能走的通，那么后面slow指针就一定能走的通


        # 这里之所以这么while条件的原因是存在主义
        # 类似于合并两个链表，while l1 and l2 意思就是说l1和l2都还存在，还没有遍历完
        # 对于单链链表而言，链表最后一个元素，进入while循环之后，item.next为空，即表示循环遍历完毕
        # 对于此题而言，我们要保证slow慢指针和fast.next快指针的后一位的同时存在，因为慢指针每次跳一位，快指针每次跳两位
            slow = slow.next
            fast = fast.next.next
            if not fast: # 当快指针走完的时候，就说明链表没有环
                return False
            if fast == slow:
                return True

        return False