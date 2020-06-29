# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
对于每一个ListNode而言，每一个实例都分成两部分，一部分是ListNode.val，另一部分是ListNode.next
ListNode.val只是一个数值，而ListNode.next则是相当于指向下一个Node的一个指针，我们要做的就是定义好这个指针，根据不同的条件把指针指向不同的Node
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) #could be ListNode(Any Number)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            else: 
                current.next = l2
                l2 = l2.next
                current = current.next
        while l1:
            current.next = l1
            current = current.next
            l1 = l1.next
        while l2:
            current.next = l2
            current = current.next
            l2 = l2.next
        
        return dummy.next