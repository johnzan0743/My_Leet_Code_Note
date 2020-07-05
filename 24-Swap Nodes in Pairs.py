# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = current_node = ListNode(0)
        dummy.next = head
        current_node.next = head
        while current_node.next and current_node.next.next:
            first = current_node.next
            second = current_node.next.next
            current_node.next = second
            first.next = second.next
            second.next = first
            current_node = current_node.next.next
        return dummy.next
        
