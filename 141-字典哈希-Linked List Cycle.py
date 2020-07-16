# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic1 = {}
        while head:
            if head not in dic1:
                dic1[head] = 1 # could be any number or anything
            else:
                return True
            head = head.next
        return False 
        # 如果while循环会跳出，那就说明head遍历结束了，也就是说明链表没有环