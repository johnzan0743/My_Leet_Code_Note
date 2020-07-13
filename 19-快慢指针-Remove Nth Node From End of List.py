# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0) #could be any number here
        slow = fast = dummy
        dummy.next = head

        #fast指针先走n次
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        # 不能写slow.next = fast 特殊情况是
        # head=[1], n=1 即fast有值而slow是空集
    
        return dummy.next
